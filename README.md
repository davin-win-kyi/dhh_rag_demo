# RAG Demo with Shape Assets & Unity Docs

This repository demonstrates how to implement a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain, OpenAI, and FAISS. We pull in documentation from:

- **Shape Assets**: [https://acegikmo.com/shapes/docs](https://acegikmo.com/shapes/docs)
- **Unity Docs**: [https://docs.unity.com/](https://docs.unity.com/)

and create a vector store of those docs to ground GPT-4o responses in real documentation.

---

## Repository Structure

```bash
├── README.md            # This file
├── requirements.txt     # Python dependencies
└── rag.py               # RAG implementation script
```

---

## Prerequisites

- **Python** 3.8+ (tested on 3.13)
- **Conda** or **venv** for environment management
- **OpenAI API Key**

---

## Installation

1. **Create & activate** (using Conda)

   ```bash
   conda create -n rag_demo python=3.13 -y
   conda activate rag_demo
   ```

2. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Set your OpenAI API key**

   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

---

## 📄 requirements.txt

The project dependencies are pinned in `requirements.txt`:

```text
aiohappyeyeballs==2.6.1
aiohttp==3.11.17
aiosignal==1.3.2
annotated-types==0.7.0
anyio==4.9.0
attrs==25.3.0
beautifulsoup4==4.13.4
bs4==0.0.2
certifi==2025.1.31
charset-normalizer==3.4.1
dataclasses-json==0.6.7
distro==1.9.0
faiss-cpu==1.10.0
frozenlist==1.6.0
greenlet==3.2.0
h11==0.14.0
httpcore==1.0.8
httpx==0.28.1
httpx-sse==0.4.0
idna==3.10
jiter==0.9.0
jsonpatch==1.33
jsonpointer==3.0.0
langchain==0.3.23
langchain-community==0.3.21
langchain-core==0.3.54
langchain-openai==0.3.14
langchain-text-splitters==0.3.8
langsmith==0.3.32
lxml==5.3.2
marshmallow==3.26.1
multidict==6.4.3
mypy-extensions==1.0.0
numpy==2.2.5
openai==1.75.0
orjson==3.10.16
packaging==24.2
playwright==1.51.0
propcache==0.3.1
pydantic==2.11.3
pydantic-core==2.33.1
pydantic-settings==2.9.1
pyee==12.1.1
python-dotenv==1.1.0
pyyaml==6.0.2
regex==2024.11.6
requests==2.32.3
requests-toolbelt==1.0.0
setuptools==75.8.0
sniffio==1.3.1
soupsieve==2.6
sqlalchemy==2.0.40
tenacity==9.1.2
tiktoken==0.9.0
tqdm==4.67.1
typing-extensions==4.13.2
typing-inspect==0.9.0
typing-inspection==0.4.0
urllib3==2.4.0
wheel==0.45.1
yarl==1.20.0
zstandard==0.23.0
```

---

## Running the Demo

Execute the RAG script to load docs, build the vector store, and ask a question:

```bash
python rag.py
```

Example output:

```
> Question: Can you give me a C# unity script that uses the shape assets library to make a red arrow
> Answer: 
using UnityEngine;
using Shapes;

[ExecuteAlways]
public class RedArrowDrawer : ImmediateModeShapeDrawer
{
    public float arrowLength = 2.0f;
    public float arrowHeadSize = 0.5f;
    public Color arrowColor = Color.red;

    public override void DrawShapes(Camera cam)
    {
        using (Draw.Command(cam))
        {
            Draw.LineGeometry = LineGeometry.Flat2D;
            Draw.ThicknessSpace = ThicknessSpace.Meters;
            Draw.Thickness = 0.1f;

            // Draw the arrow shaft
            Vector3 start = Vector3.zero;
            Vector3 end = Vector3.up * arrowLength;
            Draw.Line(start, end, arrowColor);

            // Draw the arrow head
            Vector3 arrowHeadBase = end - Vector3.up * arrowHeadSize;
            Vector3 leftHead = arrowHeadBase + Vector3.left * arrowHeadSize * 0.5f;
            Vector3 rightHead = arrowHeadBase + Vector3.right * arrowHeadSize * 0.5f;

            Draw.Line(end, leftHead, arrowColor);
            Draw.Line(end, rightHead, arrowColor);
        }
    }
}
```

Feel free to modify `rag.py` to change the question, adjust `k` (number of retrieved docs), or swap in your own documentation sources!