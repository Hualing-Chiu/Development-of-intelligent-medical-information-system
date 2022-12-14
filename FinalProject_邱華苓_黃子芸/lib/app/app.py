# 
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import taiwanesetochinese as ttc
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
# 
# 
# @app.route("/", methods = ["GET"])
# def start():
#     data = request()
#     token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDUyMzAzMzIsImlhdCI6MTY0MjE1ODMzMiwic3ViIjoiIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJpc3MiOiJKV1QiLCJ1c2VyX2lkIjoiMjk5IiwibmJmIjoxNjQyMTU4MzMyLCJ2ZXIiOjAuMSwic2VydmljZV9pZCI6IjEwIiwiaWQiOjQyNywic2NvcGVzIjoiMCJ9.mQgZ36wk8_G77l54ycPdQKDcVTOVyBHL3IDPerKpqj0hFfYMBx7x6Skuh5oHm2F9EvSOZhTZ6Tupyz5ZpUyN32p3acusuI2DBiWCxLDvQQrOuAZnfH5m5atmK_lj-PMZkLSAAz1uVnHXIjJetwrya1WOZmG6-ZSFxKNsok8OhN8"
#     toReturn = ttc.process(token,data)
#     return toReturn
# 
# 
# if __name__ == "__main__":
#     app.run(host="192.168.211.12", port="5000", debug=True)
#


from flask import Flask, request, jsonify
from flask_cors import CORS
import taiwanesetochinese as ttc
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods = ["POST"])
def start():
    data = request.get_json()
    print(data['text'])
    token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDUyMzAzMzIsImlhdCI6MTY0MjE1ODMzMiwic3ViIjoiIiwiYXVkIjoid21ta3MuY3NpZS5lZHUudHciLCJpc3MiOiJKV1QiLCJ1c2VyX2lkIjoiMjk5IiwibmJmIjoxNjQyMTU4MzMyLCJ2ZXIiOjAuMSwic2VydmljZV9pZCI6IjEwIiwiaWQiOjQyNywic2NvcGVzIjoiMCJ9.mQgZ36wk8_G77l54ycPdQKDcVTOVyBHL3IDPerKpqj0hFfYMBx7x6Skuh5oHm2F9EvSOZhTZ6Tupyz5ZpUyN32p3acusuI2DBiWCxLDvQQrOuAZnfH5m5atmK_lj-PMZkLSAAz1uVnHXIjJetwrya1WOZmG6-ZSFxKNsok8OhN8"
    result = ttc.process(token, data['text'])
    print(result)
    return result

if __name__ == "__main__":
    app.run(host="192.168.211.18", port="5000", debug=True)


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import taiwanesetochinese as ttc
# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})
#
# import mysql.connector as conn
# class CONN:
#     def __init__(self):
#         try:
#             self.connection = conn.connect(
#                 host="127.0.0.1",         # ????????????
#                 port=3306,                # ?????????
#                 user="root",              # ??????
#                 password="HouseCloud330321",          # ??????
#                 database="new_schema"           # DB??????
#             )
#             self.cursor = self.connection.cursor()
#             db_Info = self.connection.get_server_info()
#             print("??????????????????", db_Info)
#         except conn.Error as e:
#             print("??????DB?????????", e)
#
#     def __del__(self):
#         try:
#             self.cursor.close()
#             self.connection.close()
#             print("????????????????????????\n")
#         except conn.Error as e:
#             print("?????????????????????", e)
#
#     def DQL(self, sql_query):
#         try:
#             self.cursor.execute(sql_query)
#
#             #print(self.cursor.description)
#             column_name = [x[0] for x in self.cursor.description]
#             #print(self.cursor.fetchall())
#             query_result = self.cursor.fetchall()
#
#             self.connection.commit()
#
#             result = {
#                 "status": "success",
#                 "column": column_name,
#                 "result": query_result,
#                 "dml": ""
#             }
#             return result
#
#         except conn.Error as e:
#             print("???????????????", e)
#             result = {
#                 "status": "fail",
#                 "column": "None",
#                 "result": str(e),
#                 "dml": ""
#             }
#             return result
#
#     def DML(self, sql_query):
#         try:
#             self.cursor.execute(sql_query)
#             rowcount = self.cursor.rowcount
#             self.connection.commit()
#
#             table_name = None
#             dml_str = None
#             sql_query_split = sql_query.split()
#             if sql_query_split[0] == "DELETE":
#                 table_name = sql_query_split[2]
#                 dml_str = "??????{}???".format(rowcount)
#             elif sql_query_split[0] == "INSERT":
#                 table_name = sql_query_split[2]
#                 dml_str = "??????{}???".format(rowcount)
#             elif sql_query_split[0] == "UPDATE":
#                 table_name = sql_query_split[1]
#                 dml_str = "??????{}???".format(rowcount)
#
#             new_sql_query = "SELECT * FROM {}".format(table_name)
#             result = self.DQL(new_sql_query)
#             result["dml"] = dml_str
#             return result
#
#         except conn.Error as e:
#             print("???????????????", e)
#             result = {
#                 "status": "fail",
#                 "column": "None",
#                 "result": str(e),
#                 "dml": ""
#             }
#             return result
# c = CONN()
#
# @app.route("/", methods = ["GET"])
# def start():
#     print("print hello world")
#     return "F74084101 ?????????"
#
# @app.route("/mysql", methods = ["POST"])
# def mysql():
#     data = request.get_json()
#     if data["opt"] == "DQL":
#         return c.DQL(data["sql"])
#
#     error = {
#         "status": "fail",
#         "column": "None",
#         "result": "opt type error",
#         "dml": ""
#     }
#     return error
#
# if __name__ == "__main__":
#     app.run(host="140.116.119.28", port="5000", debug=True)


