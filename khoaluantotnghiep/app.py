from flask import Flask, render_template

app = Flask(__name__)

# Danh sách nhạc giả lập (Bạn có thể thay bằng database sau này)
songs = [
    {"id": 1, "title": "Sơn Tùng M-TP", "name": "Đừng Làm Trái Tim Anh Đau", "img": "https://via.placeholder.com/150"},
    {"id": 2, "title": "Đen Vâu", "name": "Nấu Ăn Cho Em", "img": "https://via.placeholder.com/150"},
    {"id": 3, "title": "tlinh", "name": "Nếu Lúc Đó", "img": "https://via.placeholder.com/150"},
    {"id": 4, "title": "HIEUTHUHAI", "name": "Ngủ Một Mình", "img": "https://via.placeholder.com/150"},
]

@app.route('/')
def home():
    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)