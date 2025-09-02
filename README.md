# Get Coin Price  
A simple desktop application developed using Python and Tkinter to fetch real-time cryptocurrency prices.  
It provides a clean and user-friendly experience for anyone who wants to quickly check coin values.  

---

## Table of Contents  

- [English Section](#get-coin-price-)  
- [Türkçe Bölüm](#get-coin-price-tr-)  

---

## Contents  

- [Overview](#overview-)  
- [Features](#features-)  
- [Installation](#installation-)  
- [Usage](#usage-)  
- [File Structure](#file-structure-)  
- [License](#license-)  
- [Author](#author-)  

---

## Overview  

This project is a **GUI-based Python application** that allows users to fetch **real-time cryptocurrency prices** via the [CoinGecko API](https://www.coingecko.com/en/api).  

Users can type the name of any coin (e.g., `bitcoin`, `ethereum`, `dogecoin`) and instantly view its price in USD.  
The app is built with **Tkinter** for the interface and **Requests** for API handling.  

---

## Features  

### Current Features  
- Simple and user-friendly **Tkinter** interface  
- Real-time data from CoinGecko  
- Search by coin name  
- Error handling for invalid coin names  
- Centered and styled GUI  

### Planned Features  
- Support for searching by **coin symbol** (e.g., BTC instead of bitcoin)  
- Multiple currency support (USD, EUR, TRY etc.)  
- Popular coin dropdown
- Themed UI improvements  

---

## Installation  

1. **Clone the repository**  
```bash
   git clone https://github.com/berkdnmz/get-coin-price.git  
   cd get-coin-price  
```
2. **Check Python version**  
   Python 3.9 or higher is recommended.
```bash
   python --version
```
3. **Install dependencies**  
```bash
   pip install requests
```

4. **Run the app**  
```bash
   python main.py
```
---

## Usage  

1. Launch the app with:  
   python main.py  
2. Enter the **coin name** (e.g., `bitcoin`) into the input box.  
3. The current price will be displayed on the screen.  
4. Press **Escape (Esc)** to exit the application.  

---

## File Structure  
```
get-coin-price/  
│  
├── main.py          # Application entry point  
├── gui.py           # Tkinter GUI class  
├── api_manager.py   # API request handler  
├── LICENSE          # License file  
└── README.md        # Documentation  
```
---

## License  

This project is open source under the [MIT License](LICENSE).  

---

## Author  

**Berk Dönmez**  

- GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
- LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)

You can contact me for any questions or suggestions regarding the project.



***Happy coding and enjoy learning lots of new coin prices!***


---

# Get Coin Price [TR]  

Python ve Tkinter kullanılarak geliştirilmiş, **gerçek zamanlı kripto para fiyatlarını** öğrenmenizi sağlayan basit bir masaüstü uygulamasıdır.  
Anlık fiyat sorgulama yapmak isteyen kullanıcılar için sade ve pratik bir çözüm sunar.  

---

## İçindekiler  

- [Genel Bakış](#genel-bakış-)  
- [Özellikler](#özellikler-)  
- [Kurulum](#kurulum-)  
- [Kullanım](#kullanım-)  
- [Dosya Yapısı](#dosya-yapısı-)  
- [Lisans](#lisans-)  
- [Yazar](#yazar-)  

---

## Genel Bakış  

Bu proje, [CoinGecko API](https://www.coingecko.com/en/api) aracılığıyla **gerçek zamanlı kripto para fiyatlarını** görüntüleyen bir Python uygulamasıdır.  

Kullanıcı arayüzü **Tkinter** ile tasarlanmış, API iletişimi ise **Requests** kütüphanesi ile sağlanmıştır.  

---

## Özellikler  

### Mevcut Özellikler  
- **Kullanıcı dostu Tkinter arayüzü**  
- CoinGecko’dan **gerçek zamanlı fiyat verileri**  
- Coin adını girerek fiyat sorgulama  
- Hatalı girişler için uyarı mesajları  
- Ortalanmış ve tasarlanmış pencere  

### Planlanan Özellikler  
- **Coin sembolüyle (BTC, ETH vb.) arama** desteği  
- Birden fazla para birimi (USD, EUR, TRY vb.) desteği  
- Popüler coinler için açılır menü
- Gelişmiş tema ve arayüz seçenekleri  

---

## Kurulum  

1. **Depoyu Klonlayın**  
```bash
   git clone https://github.com/berkdnmz/get-coin-price.git  
   cd get-coin-price  
```
2. **Python Sürümünü Kontrol Edin**  
```bash
   python --version
```
3. **Gerekli Paketleri Kurun**  
```bash
   pip install requests  
```
4. **Uygulamayı Başlatın**  
```bash
   python main.py  
```
---

## Kullanım  

1. Uygulamayı başlatmak için:  
   python main.py  
2. Kutucuğa sorgulamak istediğiniz coin adını yazın (ör. `bitcoin`).  
3. Anlık fiyat ekranda gösterilecektir.  
4. Çıkmak için **Escape (Esc)** tuşuna basın.  

---

## Dosya Yapısı  
```
get-coin-price/  
│  
├── main.py          # Uygulamanın giriş noktası  
├── gui.py           # Tkinter arayüz sınıfı  
├── api_manager.py   # API işlemleri  
├── LICENSE          # Lisans dosyası  
└── README.md        # Proje dökümantasyonu  
```
---

## Lisans  

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.  

---

## Yazar  

**Berk Dönmez**  
- GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
- LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Projeyle ilgili her türlü soru ve öneri için bana ulaşabilirsiniz.

***İyi çalışmalar ve bol coin öğrenmeli günler!***
