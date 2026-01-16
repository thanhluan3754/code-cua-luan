import time
import os
import winsound

raw_lyrics = """
Đêm mang em về trong giấc mơ
Tôi hát lên trăm lời vu vơ
Vẫn những khuôn mặt cười dù biết sẽ không hề vui
Dù hôm nay dẫu đúng sai vẫn yêu hơn ngày mai
Xin lỗi người vì những điều chưa nói ra thành câu
Xin lỗi người vì bao ngày qua đã trôi về đâu
Mất bao lâu để ta tạm quên u sầu để tim này vơi cơn đau
Và những ký ức mệt nhoài chợt tan vào sớm mai
"""

file_nhac = "music.wav"

def main():
    lines = [line.strip() for line in raw_lyrics.strip().split('\n') if line.strip()]
    
    if not os.path.exists(file_nhac):
        print(f"Lỗi: Không tìm thấy file '{file_nhac}'")
        return

    total_words = sum(len(line.split()) for line in lines)

    print("--- TOOL TẠO DATA KARAOKE V3 ---")
    print(f"Đã nhận diện: {len(lines)} câu hát - Tổng cộng {total_words} từ.")
    print("Luật chơi: Nghe nhạc -> Thấy chữ hiện ra -> Bấm ENTER ngay lập tức.")
    print("-" * 50)
    
    input(">>> Nhấn ENTER để BẮT ĐẦU nhạc...")

    winsound.PlaySound(file_nhac, winsound.SND_FILENAME | winsound.SND_ASYNC)
    start_time = time.time()
    
    ket_qua_tong = []

    try:
        for line_idx, line in enumerate(lines):
            words = line.split()
            current_line_data = []
            
            print(f"\n--- CÂU {line_idx + 1}: {line.upper()} ---")
            
            for word in words:
                print(f"Chữ: {word}  >>  (Bấm Enter)", end="\r")
                input()
                
                timestamp = round(time.time() - start_time, 2)
                current_line_data.append((timestamp, word))
                
                print(f"✅ {word} ({timestamp}s)   ")

            ket_qua_tong.append(current_line_data)

    except KeyboardInterrupt:
        print("\nĐã dừng đột ngột.")
    
    winsound.PlaySound(None, 0)

    print("\n\n" + "="*20 + " COPY ĐOẠN DƯỚI NÀY " + "="*20)
    print("lyrics_by_lines = [")
    
    for line_data in ket_qua_tong:
        print("    [")
        items = [f"({t}, \"{w}\")" for t, w in line_data]
        chunk_size = 5
        for i in range(0, len(items), chunk_size):
            chunk = items[i:i+chunk_size]
            comma = "," if (i + chunk_size < len(items)) else ""
            print("        " + ", ".join(chunk) + comma)
        print("    ],")
        
    print("]")
    print("="*60)

if __name__ == "__main__":
    main()
