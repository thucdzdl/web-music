from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# --- 1. DỮ LIỆU MẪU (DATABASE GIẢ LẬP) ---
# Danh sách bài hát dùng chung cho Trang chủ và Thịnh hành
songs = [
    {
        "id": 1, 
        "name": "Đừng Làm Trái Tim Anh Đau", 
        "title": "Sơn Tùng M-TP", 
        "img": "https://i.ytimg.com/vi/a6as_VovpSg/maxresdefault.jpg",
        "url": "/static/music/bai1.mp3"
    },
    {
        "id": 2, 
        "name": "Nấu Ăn Cho Em", 
        "title": "Đen Vâu", 
        "img": "https://i.ytimg.com/vi/S7ENm43-XGk/maxresdefault.jpg",
        "url": "/static/music/bai2.mp3"
    },
    {
        "id": 3, 
        "name": "Nếu Lúc Đó", 
        "title": "tlinh", 
        "img": "https://i.ytimg.com/vi/7v_FpGv9zYc/maxresdefault.jpg",
        "url": "/static/music/bai3.mp3"
    },
    {
        "id": 4, 
        "name": "Ngủ Một Mình", 
        "title": "HIEUTHUHAI", 
        "img": "https://i.ytimg.com/vi/q_VpYf_VvY8/maxresdefault.jpg",
        "url": "/static/music/bai4.mp3"
    }
]

# Danh sách Playlists cho trang Thư viện
playlists = [
    {"id": 1, "name": "Nhạc Trẻ Hot", "count": "15 bài hát", "img": "https://i.scdn.co/image/ab67706f00000002b60dbde074a2931ea834324f"},
    {"id": 2, "name": "Chill cuối tuần", "count": "10 bài hát", "img": "https://i.scdn.co/image/ab67706f000000025ea54a923397d3eac646067b"},
    {"id": 3, "name": "Lofi cho H2T", "count": "20 bài hát", "img": "https://i.scdn.co/image/ab67706f000000028965a397753e8a49c9044d0d"}
]

# --- 2. CÁC ĐƯỜNG DẪN (ROUTES) GIAO DIỆN ---

@app.route('/')
def home():
    # Luôn truyền current_song để Player Bar không bị lỗi undefined
    return render_template('index.html', songs=songs, current_song=songs[0])

@app.route('/trending')
def trending():
    return render_template('trending.html', songs=songs, current_song=songs[0])

@app.route('/library')
def library():
    return render_template('library.html', songs=songs, playlists=playlists, current_song=songs[0])

# --- 3. ROUTES CHO ĐĂNG NHẬP / ĐĂNG KÝ ---

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

# --- 4. LOGIC PHÁT NHẠC ---

@app.route('/play/<int:song_id>')
def play_song(song_id):
    # Tìm bài hát trong danh sách theo ID
    song = next((s for s in songs if s['id'] == song_id), None)
    if song:
        # Khi chọn bài, quay về trang chủ và cập nhật bài hát hiện tại
        return render_template('index.html', songs=songs, current_song=song)
    return abort(404)

# --- 5. USER ---
@app.route('/profile')
def profile():
    # Giả lập dữ liệu người dùng sau khi đăng nhập thành công
    user = {
        "name": "Quản trị viên H2T",
        "email": "admin@h2tmusic.com",
        "avatar": "https://ui-avatars.com/api/?name=Admin&background=1DB954&color=fff",
        "followers": "1.2K",
        "following": "150",
        "public_playlists": 5
    }
    return render_template('profile.html', user=user, songs=songs, playlists=playlists)

# --- 6. Yêu thích ---
# Thêm vào app.py
@app.route('/favorites')
def favorites():
    # Giả sử chúng ta lấy danh sách các bài hát đã thích
    # Ở đây mình dùng toàn bộ danh sách songs để hiển thị mẫu
    return render_template('favorites.html', songs=songs, current_song=songs[0])

# --- CHẠY ỨNG DỤNG ---

if __name__ == '__main__':
    # debug=True giúp tự động tải lại khi bạn thay đổi code
    app.run(debug=True, port=5000)