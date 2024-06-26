from testapp import app
from testapp import db
from datetime import datetime

class Bukken(db.Model):
    __tablename__ = 'bukken'
    id = db.Column(db.Integer, primary_key=True)  # 物件ID
    name = db.Column(db.String(255))  # 物件名
    lat = db.Column(db.Float)  # 緯度
    lng = db.Column(db.Float)  # 経度
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)  # 作成日時
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)  # 更新日時
    
    def __repr__(self):
        return 'Bukken(id={0}, name={1}, lat={2}, lng={3}, created_at={4}, updated_at={5})'.format(
            self.id, self.name, self.lat, self.lng, self.created_at, self.updated_at)

def init():
    with app.app_context():
        db.create_all()
