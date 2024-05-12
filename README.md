# LLAMA2-LLM-MODEL

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


```
$ git clone https://github.com/jcatanop/llama2-LLM-model.git
$ cd llama2-LLM-model
```

Descargue el modelo llama2 llama-2-7b-chat.ggmlv3.q8_0.bin usando el siguiente link:

```
$ wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin
```

En la carpeta actual encontrará los siguientes elementos: 

- ingest.py
- llama-2-7b-chat.ggmlv3.q8_0.bin
- model.py
- README.md
- vectorstores

Ahora podemos probar si esta funcionando:

```
$ python model.py
```

Verá el siguiente texto:

```
Ask something about pharmaceutical issues:
```

Digite la siguiente pregunta:

```
what is pharma?
```

Dependiendo de las características del computador, la respuesta puede tardar de 1 minuto o mas.

Verá algo similar a :

```
- - - - - - - - - - - -   A N S W E R   - - - - - - - - - - - - 
Answer : Farma is a term that can have different meanings depending on the context. Here are some possible interpretations of the term "farma":
1. Pharmacy: In Argentina, "farma" is used as a term for pharmacy. So, if someone asks you "¿Dónde está la farma?", they are asking where the nearest pharmacy is located.
2. Drugstore: In some Spanish-speaking countries, including Costa Rica, "farma" can also refer to a drugstore or an apothecary. So, if you're in Costa Rica and someone asks you "¿Dónde está la farma?", they might be asking where the nearest drugstore is located.
3. Medicine: In some cases, "farma" can also be used to refer to medicine or a pharmaceutical company. For example, you might hear someone say "La farma está desarrollando un nuevo medicamento para tratar la enfermedad X." (The pharmaceutical company is developing a new drug to treat disease X.)
In summary, the meaning of "farma" can vary depending on the context and location. If you'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Response time: 69.11 sec 
```

## ENTRENAR EL MODELO

Crear una carpeta con el nombre *data* en la carpeta raiz del proyecto.
Copie a la carpeta *data* los documentos PDF que contienen información para entrenar el modelo. Pueden ser libros o articulos.

Luego ejecute la siguiente orden:

```
$ python ingest.py
```

El sistema empezará a leer los archivos que haya definido y construirá la base de datos vectorial FAISS sobre la cual hará las consultas para responder preguntas.

Cuando haya terminado, pruebe a hacer una pregunta al modelo:

```
$ python model.py
```
