# LLAMA2-LLM-MODEL

Este es un LLM que puede ser entrenado para responder preguntas relacionadas a temas específicos. 

Se puede re-entrenar con nuevas fuentes de conocimiento, de manera que responda preguntas de otros campos.

Este LLM puede correr en CPU con 4G en RAM y un sistema de 64 bits.

## REQUERIMIENTOS

Requiere Python 3.8.18 y las siguientes librerias: 

- pypdf 4.2.0 
- langchain 0.1.16 
- torch 2.3.0
- accelerate  0.29.3
- bitsandbytes 0.43.1
- transformers 4.40.1
- sentence_transformers 2.7.0
- faiss_cpu 1.8.0

Para instalar las dependencias ejecute: 

```
pip install pypdf langchain torch accelerate bitsandbytes transformers sentence_transformers faiss_cpu 
```

## INSTALAR

1. Primero clone el repositorio: 

```
git clone https://github.com/jcatanop/llama2-LLM-model.git
cd llama2-LLM-model
```

2. Descargue el modelo **llama-2-7b-chat.ggmlv3.q8_0.bin** ejecutando:

```
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin
```

En la carpeta actual encontrará los siguientes elementos: 

- ingest.py
- llama-2-7b-chat.ggmlv3.q8_0.bin
- model.py
- README.md
- vectorstores

3. Crear una carpeta con el nombre **data** en la carpeta raiz del proyecto.

4. Copie a la carpeta **data** copie un (1) documento PDF que contenga información para entrenar el modelo. Puede ser un libro o articulo.

   **NOTA**: puede pegar varios PDF, pero para esta prueba, se usa un solo archivo. 

6. Para escanear los PDF ejecute la siguiente orden:

```
$ python ingest.py
```

El sistema empezará a leer los archivos PDF y construirá la base de datos vectorial (FAISS) sobre la cual hará las consultas para responder preguntas. 
Este proceso puede tomar varios minutos, dependiendo de los nucleos y RAM disponible, ademas del tamaño total de los PDF. 


## Como usar

En la carpeta raiz del proyecto ejecute:

```
$ python model.py
```

Verá el siguiente texto:

```
Ask something :
```

Ahora puede digitar una pregunta acorde con los PDF que suministro.

## Errores
Si experimenta errores al ejecutar model.py puede ser que falte alguna libreria o paquete python.
Como ultimo recurso, installe los siguientes paquetes.

```
pip install accelerate aiofiles aiohttp aiosignal altair annotated-types anyio asgiref async-timeout asyncer attrs backoff bcrypt bidict bitsandbytes build CacheControl cachetools certifi cffi chainlit charset-normalizer chevron chroma-hnswlib chromadb click coloredlogs contourpy cryptography ctransformers cycler dataclasses-json Deprecated dnspython exceptiongroup faiss-cpu fastapi fastapi-socketio ffmpy filelock filetype firebase-admin flatbuffers fonttools frozenlist fsspec google-api-core google-api-python-client google-auth google-auth-httplib2 google-cloud-core google-cloud-firestore google-cloud-storage google-crc32c google-resumable-media googleapis-common-protos gradio gradio_client graphlib_backport greenlet grpcio grpcio-status h11 httpcore httplib2 httptools httpx huggingface-hub humanfriendly idna importlib-metadata importlib_resources Jinja2 joblib jsonpatch jsonpointer jsonschema jsonschema-specifications kiwisolver  kubernetes langchain langchain-community langchain-core langchain-text-splitters langsmith Lazify literalai markdown-it-py MarkupSafe marshmallow matplotlib mdurl mmh3 monotonic mpmath msgpack multidict mypy-extensions nest-asyncio networkx numpy nvidia-cublas-cu12 nvidia-cuda-cupti-cu12 nvidia-cuda-nvrtc-cu12 nvidia-cuda-runtime-cu12 nvidia-cudnn-cu12 nvidia-cufft-cu12 nvidia-curand-cu12 nvidia-cusolver-cu12 nvidia-cusparse-cu12 nvidia-nccl-cu12 nvidia-nvjitlink-cu12 nvidia-nvtx-cu12 oauthlib onnxruntime opentelemetry-api opentelemetry-exporter-otlp opentelemetry-exporter-otlp-proto-common opentelemetry-exporter-otlp-proto-grpc opentelemetry-exporter-otlp-proto-http opentelemetry-instrumentation opentelemetry-instrumentation-asgi opentelemetry-instrumentation-fastapi opentelemetry-proto opentelemetry-sdk opentelemetry-semantic-conventions opentelemetry-util-http orjson overrides packaging pandas pillow pkgutil_resolve_name posthog proto-plus protobuf psutil py-cpuinfo pyasn1 pyasn1_modules pycparser pydantic pydantic_core pydub Pygments PyJWT pymongo pyparsing pypdf PyPika pyproject_hooks python-dateutil python-dotenv python-engineio python-graphql-client python-multipart python-socketio pytz PyYAML referencing regex requests requests-oauthlib rich rpds-py rsa ruff safetensors scikit-learn scipy semantic-version sentence-transformers setuptools shellingham simple-websocket six sniffio SQLAlchemy starlette sympy syncer tenacity threadpoolctl tiktoken tokenizers tomli tomlkit toolz torch tqdm transformers triton typer typing_extensions typing-inspect tzdata uptrace uritemplate urllib3 uvicorn uvloop watchfiles websocket-client websockets wrapt wsproto yarl zipp                                     
```
