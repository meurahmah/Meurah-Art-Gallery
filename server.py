from flask import Flask, render_template, request

app = Flask(__name__)

# Data Karya
karya_list = [
    {"judul": "Valrama Al", "tahun": 2022, "gambar": "gambar1.png"},
    {"judul": "Seleksi Lomba", "tahun": 2023, "gambar": "gambar2.jpg"},
    {"judul": "My Shaylaa(2)", "tahun": 2024, "gambar": "gambar3.png"},
    {"judul": "Vallum", "tahun": 2021, "gambar": "gambar4.png"},
    {"judul": "My Favorite", "tahun": 2023, "gambar": "gambar5.jpg"},
    {"judul": "Alfie", "tahun": 2021, "gambar": "gambar6.jpg"},
    {"judul": "Soshiro Hoshina", "tahun": 2024, "gambar": "gambar7.jpg"},
    {"judul": "My Shaylaa", "tahun": 2023, "gambar": "gambar8.png"},
    {"judul": "DTIYS", "tahun": 2020, "gambar": "gambar9.jpg"},
    {"judul": "Alfiee", "tahun": 2020, "gambar": "gambar10.jpg"},
    {"judul": "Almeera", "tahun": 2022, "gambar": "gambar11.jpg"},
    {"judul": "Cutiess", "tahun": 2025, "gambar": "gambar12.png"},
    {"judul": "Kalea<3", "tahun": 2025, "gambar": "gambar13.png"},
    {"judul": "Griffith", "tahun": 2024, "gambar": "gambar14.jpg"},
    {"judul": "Seleksi FLS2N", "tahun": 2023, "gambar": "gambar15.jpg"},
    {"judul": "Ref Sketch", "tahun": 2024, "gambar": "gambar16.png"},
    {"judul": "Sketch Practice", "tahun": 2024, "gambar": "gambar17.png"},
    {"judul": "Random", "tahun": 2024, "gambar": "gambar18.png"}
]

@app.route('/')
def index():
    tahun_filter = request.args.get('tahun')
    if tahun_filter:
        karya = [k for k in karya_list if str(k['tahun']) == tahun_filter]
    else:
        karya = karya_list
    return render_template('start.html', karya=karya)

if __name__ == '__main__':
    app.run(host='192.168.100.134', port=5000, debug=True)
