from django.shortcuts import render
from django.http import Http404

# Data Dummy Toko Sepatu Premium
DATA_SEPATU = {
    # Setiap kunci (key) dalam dictionary ini adalah ID unik sepatu.
    1: {
        'id': 1,
        'nama': 'Air Max Neo-Chrono',
        'kategori': 'Running / Casual',
        'harga': 'Rp 2.499.000',
        'deskripsi': 'Didesain untuk kecepatan dan kenyamanan maksimal. Menggunakan teknologi bantalan udara mutakhir yang memberikan respons pengembalian energi di setiap langkah Anda.',
        'gambar': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600',
        'ukuran': [39, 40, 41, 42, 43, 44],
        'stok': 5
    },
    2: {
        'id': 2,
        'nama': 'Court Classic Retro',
        'kategori': 'Streetwear / Lifestyle',
        'harga': 'Rp 1.899.000',
        'deskripsi': 'Siluet klasik yang terinspirasi dari era lapangan tenis tahun 80-an. Dibuat dengan kulit premium bertekstur lembut untuk tampilan estetik yang tak lekang oleh waktu.',
        'gambar': 'https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=600',
        'ukuran': [40, 41, 42, 43],
        'stok': 3
    },
    3: {
        'id': 3,
        'nama': 'VaporFly Elite Sport',
        'kategori': 'Professional Racing',
        'harga': 'Rp 3.199.000',
        'deskripsi': 'Sepatu balap lari jarak jauh andalan para juara. Dilengkapi dengan pelat serat karbon internal yang mendorong Anda melesat ke depan dengan efisiensi energi tertinggi.',
        'gambar': 'https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=600',
        'ukuran': [41, 42, 43, 45],
        'stok': 2
    }
}

def index(request):
    print(f"DEBUG: Mengakses index dengan {len(DATA_SEPATU)} data sepatu")
    context = {'sepatu_list': DATA_SEPATU.values()}
    return render(request, 'index.html', context)

def detail(request, sepatu_id):
    sepatu = DATA_SEPATU.get(sepatu_id)
    if not sepatu:
        raise Http404("Sepatu tidak ditemukan")
    context = {'sepatu': sepatu}
    return render(request, 'detail.html', context)