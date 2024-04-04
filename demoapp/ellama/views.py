from django.shortcuts import render
import ollama

def chat_view(request):
    if request.method == 'POST':
        prompt= request.POST.get('promt')
        response= ollama.chat(model='illama2',messages=[{'role':'user','content':'why sky is looking blue colour?'}])
        generated_response=response['message']['content']
        return render(request, 'ellama/chat.html', {'prompt': prompt, 'generated_response': generated_response})
    else:
        return render(request, 'ellama/chat.html')
