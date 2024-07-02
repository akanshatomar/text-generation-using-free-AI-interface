import cohere
from flask import Flask, render_template, request, redirect, url_for
from groq import Groq
import cohere
co = cohere.Client('mVs7XgINhhFUGB3NlyWQRo6HPFz9rcqKybPu3FuS')

app = Flask(__name__)


client = Groq(
    api_key="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"
)
def cohere_result(question):
     response = co.generate(
            model='command-nightly',
            prompt=question,
            max_tokens=300,
            temperature=0.9,
            k=0,
            p=0.75,
            stop_sequences=[],
            return_likelihoods='NONE'
        )
     return response.generations[0].text

def groqcloud_result(question):
     chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )
     return chat_completion.choices[0].message.content


@app.route('/', methods =["GET", "POST"])
def home():
    output_groqcloud = None
    output_cohere = None
    if request.method == "POST":
       sample_input = request.form.get("input")
       output_groqcloud = groqcloud_result(sample_input)
       output_cohere = cohere_result(sample_input)
       f = open("demo_file.txt", "a")
       f.write(sample_input)
       f.write("\ngrodcloud: " + output_groqcloud + "\n\n")
       f.write("\ncohere: " + output_cohere + "\n\n")
       f.write("*************")
       f.write("/n")
       f.close()
       return render_template("index.html", output_groqcloud = output_groqcloud, output_cohere= output_cohere)
    return render_template("index.html", output_cohere = None, output_groqcloud = None)

 

if __name__ == "__main__":
	app.run(debug=True)