# LLAMA2-PHARMA

Este es un LLM pre-entrenado para responder preguntas relacionadas a temas farmacéuticos. 

Se puede re-entrenar con nuevas fuentes de conocimiento, de manera que responda preguntas de otros campos.

Este LLM puede correr en CPU con 4G en RAM y un sistema de 64 bits.

## REQUERIMIENTOS

Requiere Python 3.8.18 y las siguientes librerias: 

```
pip install pypdf 4.2.0
    langchain 0.1.16 \
    torch 2.3.0 \ 
    accelerate  0.29.3 \
    bitsandbytes 0.43.1 \
    transformers 4.40.1 \
    sentence_transformers 2.7.0 \
    faiss_cpu 1.8.0
```

## INSTALAR Y TESTEAR

Primero clone el repositorio: 


```$ git clone https://github.com/jcatanop/llama2-LLM-model.git
$ cd llama2-LLM-model```

Descargue el modelo llama2 llama-2-7b-chat.ggmlv3.q8_0.bin usando el siguiente link:

```$ wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin```

En la carpeta actual encontrará los siguientes elementos: 

- data
- ingest.py
- llama-2-7b-chat.ggmlv3.q8_0.bin
- model.py
- README.md
- vectorstores

Ahora podemos probar si esta funcionando:

```$ python model.py```

Verá el siguiente texto:

```Ask something about pharmaceutical issues:```

Digite la siguiente pregunta:

```what is pharmaceutics?```

Dependiendo de las características del computador, la respuesta puede tardar de 1 minuto o mas.

Verá algo similar a :

``` - - - - - - - - - - - -   A N S W E R   - - - - - - - - - - - - 
Answer: Pharmaceutics is a branch of the health sciences that deals with the scientific aspects of drugs, including their composition, manufacture, storage, quality control, and delivery to patients. It encompasses various disciplines such as biopharmaceutics, pharmacokinetics, and pharmacodynamics, which are essential for understanding how drugs interact with the body and how they can be used safely and effectively to treat various diseases and medical conditions. Pharmaceutics is a fundamental subject in pharmacy education and is critical for the development of new drugs and the optimal use of existing ones.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Response time: 63.56 sec```
 

## ENTRENAR EL MODELO

Copie a la carpeta ``data`` los documentos PDF que contienen información para entrenar el modelo.
Luego ejecute la siguiente orden:

```$ python ingest.py ```

El sistema empezará a leer los archivos que haya definido y construirá la base de datos vectorial FAISS sobre la cual hará las consultas para responder preguntas.

Cuando haya terminado, pruebe a hacer una pregunta al modelo:

```$ python model.py```
