from flask import Flask, request

import csv
app=Flask(__name__)
@app.route("/otabek",methods=['Post'])
def main():
  

    if request.method == "POST" :
        data=request.get_json()
   
    f=open('users.csv',mode='a')
    writer = csv.writer(f)
    if data and type(data[0])==dict:
       for i in data:
          writer.writerow(i.values())
       return  {"message": "Data added", "data": data}
    return {'status_code':'Error'}
    




if __name__=='__main__':
    app.run(debug=True,port=8000)