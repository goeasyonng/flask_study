from flask.mysql import MySQL
from flask import Flask
from flask import jsonify
from flask import request
import random

board = Flask(__name__)

mysql=MySQL()
app.comfig['MYSQL_DATABASE_BOARD']='dbmasteruser'
app.config['MYSQL_DATABASE_PASSWORD']= '123123123'
app.config['MYSQL_DATABASE_HOST']='ls-ed7c6cfd2a9a01bf9411cda04bb53b7583775cb8.ce9zqwpjj5xx.ap-northeast-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_DB']='db1'
mysql.init_board(board)

@app.route("/generate_board", method=['GET'])
def bordGenerate():
    
    conn=mysql.connect()
    cursor=conn.cursor()
    
    for i in range(100):
    
        titles_list=["title1","title2","title3"]
        title = random.choice(title_list)
        
        content_list = ["내용1", "내용2","내용3"]
        content = random.choice(content_list)
        
        likes=str(random.randrange(1,100,3))
        
        img = "www.img.com/"+str(random.randrange(1,99,1))
        
        created = str(datetime.datetime.now())
        user_id=str(random.randrange(43,173,1))
        
        cursor.execute(
            f"""
            INSERT INTO board(title, content, likes, img, created, user_id)
            VALUES('{title}','{content}','{likes}','{img}','{created}','{user_id}')
            """
            )
                
        conn.commit()
            
    cursor.close()
    conn.close()
        
    return jsonify({'result':"success"})                            