# from flask import Flask

# app=Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<h1>Hello World</h1>"

# @app.route("/project")
# def show_project():
#     return "<h1>This is project page</h1>"

# @app.route("/about")
# def show_about():
#     return "<h1>This is project page</h1>"

# @app.route("/feeds/<int:feed_id>")
# def show_one_feed(feed_id):
#     return f"<h1>Feed ID : {feed_id}</h1>"

# @app.route("/<name>")
# def hello_name(name):
#     return f"Hello, {name}!"

# @app.route("/myinfo/<username>")
# def show_my_info(username):
#     return f"<h1>Username is {username}"

# # 유저가 보낸 데이터가 requset에 담겨서 온다.
# from flask import request
# # 서버에서 유저에게 데이터를 보내기 위해 사용
# from flask import jsonify

# @app.route('/api/v1/feeds', methods=['GET'])
# def show_all_feeds():
#     data={
#         "title":"제목",
#         "img":"www.image.com/1",
#         "like":"100",
#         "reviews":[
#             {"id":1,"nickname":"leo","content":"댓글1"},
#             {"id":2,"nickname":"leo","content":"댓글2"},
#             {"id":3,"nickname":"leo","content":"댓글3"},
#             {"id":4,"nickname":"leo","content":"댓글4"},
#             {"id":5,"nickname":"leo","content":"댓글5"},
            
#         ]
#     }
    
#     print(type(data))
#     print(type(jsonify(data)))

#     return jsonify(data)

# # 게시글 하나 조회
# @admin.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
# def show_one_feed(feed_id):
#     print(feed_id)
#     return jsonify({'result':'success', 'data': {"feed1":"data"}})

# # 게시글 생성
# from flask import requset
# @app.route('/api/v1/feeds', methods=['POST'])
# def create_one_feed():
#     name = request.form['name']
#     age = requset.form['age']
    
#     print(name,age)
#     return justify({"result":"success"})

# #db커넥트
# from flasktext.mysql import MySQL

# mySQL=MySQL()
# app.config['MYSQL_DATABASE_USER']='dbmasteruser'
# app.config['MYSQL_DATABASE_PASSWORD']='123123123'
# app.config['MYSQL_DATABASE_DB']=''
# app.config['MYSQL_DATABASE_HOST']='ls-ed7c6cfd2a9a01bf9411cda04bb53b7583775cb8.ce9zqwpjj5xx.ap-northeast-2.rds.amazonaws.com'
# mysql.init_app(app)

# conn=mysql.connect()
# cursor=conn.cursor()
# cursor.execute(
    
# )

# datas = sursor.fetchall()

# conn.commit()
# cursor.close()
# conn.close()


# # 유저 부분
# from flask import request
# @app.route('/api/v1/users',methods=['GET','POST','PUT','DELETE'])
# def users():
#     conn = mysql.connect()
#     cursor=conn.cursor()
    
#     if(requset.method=="GET"):#유저 조회
#         curson.execute("""SELECT*from user""")
#         results=cursor.fetchall()
#         return jsonify({'result':results})
    
#     elif(requset.method=="POST"):#유저 생성
#         name-request.form['name']
#         age=requset.form['age']
        
#         curson.excute()
#         conn.commit()
#         conn.close()
#         return isonify({'result':"success"})
    
#     elif(requset.method=="PUT"):#유저 업데이트
#         name=request.form['name']
#         age=request.form['age']
        
#         conn.commit()
#         cursor.close()
#         conn.close()
#         return justify({'result':"success"})
    
#     elif(requset.method=="DELETE"):#유저 삭제
#         return    

@app.route("/generate_board")
def bordGenerate():
    
    titles_list=["title1","title2","title3"]
    title = random.choice(title_list)
    
    content_list = ["내용1", "내용2","내용3"]
    content = random.choice(content_list)
    
    likes=str(random.randrange(1,100,3))
    
    img = "www.img.com/"+str(random.randrange(1,99,1))
    
    created = str(datetime.datetime.now())
    user_id=str(random.randrange(43,173,1))
    