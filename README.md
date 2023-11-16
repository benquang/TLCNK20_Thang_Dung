# Data Process
Data Source: fbreb, sofifa
Quá trình xử lý data về các statistics các maches qua 5 mùa (2018-2023) được thực hiện thông qua các bước:
- prepare.ipynb: sửa tên các attribute, định dạng kiểu dữ liệu, chọn lọc các attribute cần thiết,... (kết quả được lưu trong fbref_modified và sofifa_modified) 
- analysis.ipynb: thay đổi các statistics, kết hợp các statistics giữa fbref và sofifa (kết quả được lưu trong merge)
- model_dataset.ipynb: tính toán các statistics của sofifa players, tạo dataset các matchs dùng cho xây dựng model (kết quả được lưu trong dataset_model)
