from app import User,db,app

with app.app_context():
    # 一度すべてのテーブルを削除し、再作成
    db.drop_all()
    db.create_all()

    user1 = User('admin_user1@test.com', 'Admin User1', '111', '1')
    user2 = User('test_user1@test.com', 'Test User1', '111', '0')

    db.session.add_all([user1, user2])
    db.session.commit()

    print(user1.id)
    print(user2.id)
