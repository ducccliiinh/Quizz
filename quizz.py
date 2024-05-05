print("Welcome to game")
name = input('Type your name:')
print('START!')
cauhoi = ["Câu 1: Khẳng định nào sau đây về Python là đúng?\n A.Python là một ngôn ngữ lập trình cấp cao.\n B.Python là một ngôn ngữ thông dịch.\n C.Python là ngôn ngữ lập trình hướng đối tượng.\n D.Tất cả các đáp án đều đúng", 
          "Câu 2: Kí hiệu nào dùng để xác định các khối lệnh (khối lệnh của hàm, vòng lặp,...) trong Python?\n A.Dấu ngoặc nhọn { }\n B.Dấu ngoặc vuông [ ]\n C.Thụt lề\n D.Dầu ngoặc đơn ( )", 
          "Câu 3: Khẳng định nào là đúng về chú thích trong Python?\n A.Chú thích giúp cho các lập trình viên hiểu rõ hơn về chương trình.\n B.Trình thông dịch Python sẽ bỏ qua những chú thích.\n C.Có thể viết chú thích trên cùng một dòng với lệnh/biểu thức hoặc viết trên nhiều dòng mà không vấn đề gì cả\n D.Tất cả các đáp án trên.", 
          'Câu 4: Đâu là quy tắc đúng khi đặt tên cho biến trong Python?\n A.Tên biến có thể bắt đầu bằng dấu gạch dưới "_".\n B.Có thể sử dụng keyword làm tên biến.\n C.Tên biến có thể bắt đầu bằng một chữ số.\n D.Tên biến có thể có các ký hiệu như !, @, #, $, %,... ',
          "Câu 5: n trong đoạn sau là kiểu dữ liệu nào? \n n ='5'\n A.integer\n B.string\n C.tuple\n D.operator",
          "Câu 6: Output của lệnh sau là:\n print(1, 2, 3, 4, sep='*')\n A.1 2 3 4\n B.1234\n C.1*2*3*4\n D.24",
          "Câu 7: Kết quả của đoạn code dưới đây là:\n numbers = [2, 3, 4]\n print(numbers)\n A.2, 3, 4\n B.2 3 4\n C.[2, 3, 4]\n D.[2 3 4]",
          "Câu 8: Kết quả của code sau là:\n for x in range(0.5, 5.5, 0.5):\n    print(x)\n A.[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]\n B.[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]\n C.[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]\n D.Chương trình lỗi",
          "Câu 9: Kết quả của code sau là gì?\n x = 36 / 4 * (3 +  2) * 4 + 2\n  print(x)\n A.182.0\n B.37\n C.117\n D.Chương trình bị lỗi",
          'Câu 10: Kết quả của code sau là gì?\n sampleList = ["Jon", "Kelly", "Jessa"]\n sampleList.append(2, "Scott")\n print(sampleList)\n A.Chương trình bị lỗi\n B.[‘Jon’, ‘Kelly’, ‘Scott’, ‘Jessa’]\n C.[‘Jon’, ‘Kelly’, ‘Jessa’, ‘Scott’]\n D.[‘Jon’, ‘Scott’, ‘Kelly’, ‘Jessa’]']

dapan = ["D", "C", "D", "A", "B", "C", "C", "D", "A", "A"]
diem = 0
tien = 0
for i in range(len(cauhoi)):
    print(cauhoi[i])
    cautraloi = input("Choose A, B, C or D:")
    if cautraloi == dapan[i]:
        print("Correct!")
        diem += 1
        tien += 1000
    else:
        print("Wrong!")
        tien -= 500
    print('\n')

print(name, "point:", diem, 'money:', tien)
