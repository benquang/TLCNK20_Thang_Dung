# Football Crawling

# Data Process
Data Source: <a href="https://github.com/benquang/TLCNK20_Thang_Dung/tree/master/data_processing/fbref">fbreb</a>, <a href="https://github.com/benquang/TLCNK20_Thang_Dung/tree/master/data_processing/sofifa">sofifa</a> <br>
Quá trình xử lý data về các statistics các maches qua 5 mùa (2018-2023) được thực hiện thông qua các bước:
- prepare.ipynb: sửa tên các attribute, định dạng kiểu dữ liệu, chọn lọc các attribute cần thiết,... (kết quả được lưu trong <a href="https://github.com/benquang/TLCNK20_Thang_Dung/tree/master/data_processing/fbreb_modified">fbreb_modified</a> và <a href="https://github.com/benquang/TLCNK20_Thang_Dung/tree/master/data_processing/sofifa_modified">sofifa_modified</a>) 
- analysis.ipynb: thay đổi các statistics, kết hợp các statistics giữa fbref và sofifa (kết quả được lưu trong <a href="https://github.com/benquang/TLCNK20_Thang_Dung/tree/master/data_processing/merge">merge</a>)
- model_dataset.ipynb: tính toán các statistics của sofifa players, tạo dataset các matchs dùng cho xây dựng model (kết quả được lưu trong <a href="https://github.com/benquang/TLCNK20_Thang_Dung/tree/master/data_processing/dataset_model">dataset_model</a>)

# Football Predicting
Xây dựng model dự đoán result khả quan cho các match<br>

