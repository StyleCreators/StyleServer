import os

from flask import Flask,request,Response,send_from_directory

app=Flask(__name__)
@app.route('/<path:name>', methods=['GET','POST'])
def upload_file(name):
    style = request.args.get('styletype')
    filename = request.args.get('filename')
    print(style)
    print(filename)
    img = request.data
    with open('./upload_pic/' + filename + '.jpeg','wb') as file:
        file.write(img)
        file.flush()
    print('Save img')
    s=''
    s='python eval.py --model_file ./model/' + str(style) + ' --image_file ./upload_pic/' + filename + '.jpeg'+' --filename '+str(filename)
    print(s)
    os.system(s)
    print('ok')
    return 'http://192.168.6.141:5000/images/'+filename+'.jpeg'
@app.route('/images/<path:filename>', methods=['GET','POST'])
def get_pic(filename):
    print("get+pic!!!!!!!!!!!!!!!!!!!!!!")
    return send_from_directory('./images',filename)
if __name__ == '__main__':
    app.run('192.168.6.141')
