import re
import json
from flask import Flask, render_template, request, jsonify
import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA

app = Flask(__name__)

# --- Backend Vector DB / LLM setup ---
groq_api_key = os.environ.get("GROQ_API_KEY")
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./db", embedding_function=embedding_function)
llm = ChatGroq(
    api_key=groq_api_key,
    model_name="gemma2-9b-it",
    temperature=0.7,
    max_tokens=1024
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# --- Flask Routes ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tender_text = request.form.get('tender')
        # build prompt
        prompt = f'''
        TENDER TITLE: {tender_text} Given a tender title and a machinery corpus containing detailed specifications for machines like SJE 10 LM/XL, CNC Milling, CNC Lathes, Water Jet Cutters, and others, perform the following tasks: 
        Retrieve Relevant Machinery: Identify atleast 3 machines from the corpus that are most likely to fulfill the requirements implied by the tender title. Consider the tender's potential material, precision, and operational needs.
        Assign Possibility to Use Score: For each selected machine, provide a score from 0 to 100 indicating the likelihood that it can meet the tender requirements. Base the score on:
        Compatibility with materials and tolerances suggested by the tender title.
        Machine specifications (e.g., spindle speed, work envelope, accuracy).
        Feasibility of using the machine as-is or with minimal modifications.
        Explain Suitability: For each machine, provide a concise explanation (200-300 words) detailing:
        How the machine's features align with the tender's implied requirements.
        Whether the machine can be used as-is, requires minor modifications (e.g., tooling upgrades), or needs significant upgrades.
        Estimated cost implications (qualitative, e.g., low, moderate, high) for modifications or upgrades.
        Any limitations or risks in using the machine for the tender.
        The Output Format:
        Return the results only in a structured json format nothing more nothing less:
        ```json
        {{
            "machines": [
            {{
                "name": "Machine Name",
                "possibility_score": 85,
                "explanation": "Concise explanation of suitability."
            }}
            ]
        }}
        ```
        '''
        result = qa_chain.invoke({"query": prompt})["result"]
        result = re.search(r'{.*}', result, re.DOTALL)
        if result:
            result = json.loads(result.group(0))
        else:
            result = {"machines": []}
        try:
            machines = result
        except Exception:
            machines = result
        return render_template('index.html', machines=machines, tender=tender_text)
    return render_template('index.html', machines=None)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
