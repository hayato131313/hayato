from app import db,User,app

user_list=[]
for i in range(60):
    user_list.append(User(f'temp_user{i}test.com',f'Temp User{i}','111',0))

with app.app_context():
    db.session.add_all(user_list)
    db.session.commit()
    print('60人のテストユーザーを追加しました。')