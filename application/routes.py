from application import app
import bot
from flask import render_template ,request 




@app.route('/')
@app.route('/home')
@app.route('/index')
def hello_world():
     return render_template("index2.html")

@app.route('/get')
def form_post():
    
        message = request.args.get('msg')
        response = bot.chat(message)
        return str(response)    

        
#   if request.method == 'POST' : 
#      message = request.form['usermsg']
#      update_html.update(message,'user')
#      render_template('index2.html')
#      reply=bot.chat(message)
#      update_html.update(reply,'bot')
#      return render_template('index2.html')

