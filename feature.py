from flask import Flask,render_template

FAI=Flask(__name__)#FLASK APPLICATION INSTANCE

@FAI.route('/first_html')
def first_html():
    return render_template('first_html.html',name='Ramesh')


@FAI.route('/second_html')
def second_html():
    return render_template('second_html.html')

if __name__=='__main__':
    FAI.run(debug=True)