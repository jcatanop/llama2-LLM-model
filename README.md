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

