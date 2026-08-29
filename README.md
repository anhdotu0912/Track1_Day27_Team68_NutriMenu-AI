# Track 1 - Day 27 — AI Team Lab

- **Team:** Team 68
- **Thành viên (3–5 người):**
  1. **Đỗ Tú Anh** — MSSV: `2A202601272` _(Trưởng nhóm / Quản lý sản phẩm)_
  2. **Trần Thanh Huyền** — MSSV: `2A202601578` _(Kỹ sư AI chính)_
  3. **Thiều Thị Ngọc Ánh** — MSSV: `2A202601864` _(Kỹ sư Dữ liệu, Backend & Kiểm thử)_
- **Tên dự án:** **NutriMenu AI** — Trợ lý AI Kiểm tra Dinh dưỡng & Cảnh báo Dị ứng Thực đơn Bán trú
- **Link sản phẩm/demo (nếu có):** `https://github.com/anhdotu0912/Track1_Day27_Team68_DuAn68`

---

## 📌 Phase 0: Chốt Phạm vi & Cách làm việc chung

### 1. Thành viên trong nhóm (Team 68)

- **Số lượng:** 3 người.
- **Phân chia công việc:**
  - **Đỗ Tú Anh:** Trưởng nhóm, phụ trách kết nối với các trường, viết tài liệu, quản lý repo và nộp bài.
  - **Trần Thanh Huyền:** Phụ trách phần AI, viết prompt, kết nối dữ liệu món ăn và kiểm tra độ chính xác của mô hình.
  - **Thiều Thị Ngọc Ánh:** Phụ trách xử lý dữ liệu dinh dưỡng từ Viện Dinh Dưỡng, viết API backend và chạy test các trường hợp thực tế.

---

### 2. Dự án nhóm làm là gì?

- **Tên dự án:** **NutriMenu AI**
- **Vấn đề thực tế:** Mỗi tuần, các bếp ăn trường tiểu học phải lên thực đơn cho hàng trăm học sinh. Việc tính calo, đạm, đường, béo bằng tay rất mất thời gian. Đáng lo nhất là chuyện **học sinh bị dị ứng** (như dị ứng lạc/đậu phộng, tôm cua, sữa, trứng, bột mì). Chỉ cần đầu bếp sơ suất dùng gia vị có thành phần ẩn là có thể gây nguy hiểm cho học sinh.
- **Cách giải quyết:** Nhóm làm một công cụ AI để đọc file thực đơn tuần (Excel/ảnh chụp), đối chiếu với bảng thành phần món ăn chuẩn của Viện Dinh Dưỡng Quốc Gia. AI sẽ tự tính nhanh calo/vi chất và gắn cờ cảnh báo đỏ ngay nếu thấy có món chứa chất dễ gây dị ứng.

---

### 3. Mục tiêu cụ thể trong 1–3 tháng tới

- **Tháng 1:** Hoàn thành bản thử nghiệm đầu tiên (MVP), đọc được file thực đơn Excel và phát hiện chính xác các nhóm dị ứng phổ biến theo quy định y tế.
- **Tháng 2:** Tính toán chuẩn năng lượng theo từng độ tuổi (Mầm non: 3–5 tuổi; Tiểu học: 6–11 tuổi), mức lệch calo và dinh dưỡng không quá 5%.
- **Tháng 3:** Đưa vào dùng thử tại 03 trường tiểu học bán trú, giúp Bếp trưởng và Ban Giám hiệu giảm bớt thời gian duyệt thực đơn mỗi tuần.

---

### 4. Quy ước nộp bài

- Toàn bộ bài làm được lưu tại `README.md` trên GitHub repo: `Track1_Day27_Team68_DuAn68`.
- Xuất file PDF tóm tắt 4 trang (`Day27_AI-Team-Lab_Team68.pdf`) đính kèm trong repo.
- Người chịu trách nhiệm nộp bài: Đỗ Tú Anh.

---

### 🚦 GATE 0: Kiểm tra chốt phạm vi

| Câu hỏi kiểm tra                                       | Đánh giá | Chi tiết                                                                |
| :----------------------------------------------------- | :------: | :---------------------------------------------------------------------- |
| Cả nhóm có đang làm cùng một dự án không?              |  ✅ Đạt  | Dự án NutriMenu AI                                                      |
| Mục tiêu 1–3 tháng có rõ ràng không?                   |  ✅ Đạt  | Có số liệu cụ thể: quét dị ứng, tính calo <5% lệch, thử nghiệm 3 trường |
| Đã phân công người chịu trách nhiệm tổng hợp bài chưa? |  ✅ Đạt  | Đỗ Tú Anh phụ trách repo và nộp bài                                     |
| Số lượng thành viên hợp lệ?                            |  ✅ Đạt  | Đúng 3 thành viên                                                       |

---

## 🗺️ Phase 1: Bản đồ Stakeholder & Chiến lược Tiếp cận (Trang 1 / 4 PDF)

### 1. Danh sách 7 bên liên quan cụ thể quanh dự án

1. **Cô Hoàng Lan (Hiệu trưởng Trường Tiểu học):** Người có tiếng nói quyết định xem trường có cho phép dùng thử phần mềm hay không.
2. **Chú Nguyễn Văn Bình (Bếp trưởng trường bán trú):** Người trực tiếp gõ thực đơn, tính tiền chợ và nấu nướng cho học sinh mỗi ngày.
3. **TS. BS. Vũ Thu Trang (Bác sĩ Viện Dinh Dưỡng Quốc Gia):** Chuyên gia tư vấn về chuẩn định lượng bữa ăn học đường cho trẻ em Việt Nam.
4. **Chị Lê Mai Anh (Trưởng ban Phụ huynh trường):** Phụ huynh có con nhỏ bị dị ứng đậu phộng, rất lo lắng về an toàn suất ăn ở trường.
5. **Y sĩ Trần Quốc Bảo (Nhân viên Y tế trường học):** Người nắm danh sách học sinh có tiền sử dị ứng và sơ cứu nếu có sự cố.
6. **Thầy Nguyễn Tuấn Anh (Giảng viên / Mentor hướng dẫn):** Người góp ý kỹ thuật mô hình AI và hỗ trợ kết nối nhóm với các trường học.
7. **Anh Đặng Quốc Cường (Giám đốc công ty cung cấp suất ăn bên ngoài):** Đơn vị nấu ăn theo hợp đồng cho một số trường trên địa bàn.

---

### 2. Sắp xếp vị trí trên Ma trận (Ảnh hưởng × Mức quan tâm & Thái độ)

```
                     Mức độ quan tâm (Interest)
                     THẤP ───────────────────► CAO
        ┌─────────────────────────────┬─────────────────────────────┐
        │ [BLOCKER - CẦN THUYẾT PHỤC] │ [CHAMPION - ỦNG HỘ CHÍNH]   │
     C  │                             │                             │
     A  │ • Cô Hoàng Lan (Hiệu trưởng)│ • Thầy Nguyễn Tuấn Anh      │
     O  │   Thái độ: ⚠️ Đang lo ngại  │   (Mentor hướng dẫn)        │
        │   (Sợ AI sai sót gây rủi ro)│   Thái độ: 🟢 Ủng hộ nhiệt tình│
Ả       │                             │ • TS. BS. Vũ Thu Trang      │
n       │                             │   (Bác sĩ Viện Dinh Dưỡng)  │
h       │                             │   Thái độ: 🟢 Ủng hộ        │
        ├─────────────────────────────┼─────────────────────────────┤
h       │ [BYSTANDER - THEO DÕI]      │ [SUPPORTER - ỦNG HỘ & GÓP Ý]│
ư       │                             │                             │
ở       │ • Anh Đặng Quốc Cường       │ • Chú Nguyễn Văn Bình       │
n       │   (Giám đốc cty suất ăn)    │   (Bếp trưởng)              │
g       │   Thái độ: ⚪ Chưa quan tâm │   Thái độ: 🟢 Rất ủng hộ    │
        │                             │ • Chị Lê Mai Anh (Phụ huynh)│
     T  │                             │   Thái độ: 🟡 Cẩn trọng     │
     H  │                             │ • Y sĩ Trần Quốc Bảo (Y tế) │
     Ấ  │                             │   Thái độ: 🟢 Ủng hộ        │
     P  │                             │                             │
        └─────────────────────────────┴─────────────────────────────┘
```

#### Đánh giá thực tế từng nhóm:

- **Nhóm Ủng hộ chủ chốt (Champion):** Thầy Mentor và Bác sĩ Dinh dưỡng. Có uy tín chuyên môn cao, hiểu giá trị của việc tự động hóa dinh dưỡng và sẵn sàng hỗ trợ nhóm.
- **Nhóm Cần thuyết phục nhất (Blocker):** Cô Hiệu trưởng. Cô có quyền duyệt cao nhất nhưng e ngại rủi ro trách nhiệm nếu AI báo sai khiến học sinh bị dị ứng.
- **Nhóm Ủng hộ & Góp ý (Supporter):** Chú Bếp trưởng và Chú Y sĩ ủng hộ vì giúp họ bớt việc vất vả; Chị Phụ huynh quan tâm sát sao nhưng cần thấy minh bạch rõ ràng.
- **Nhóm Ít liên quan (Bystander):** Giám đốc công ty suất ăn bên ngoài, hiện tại chỉ theo dõi khi nhà trường có yêu cầu bắt buộc.

---

### 3. Kế hoạch hành động cụ thể cho 4 bên ưu tiên (1–2 tuần tới)

| Người liên quan                              | Phân nhóm & Thái độ                      | Họ quan tâm điều gì nhất?                                                                         | Thuận lợi / Trở ngại cho nhóm?                                                                                 | Việc nhóm cần làm ngay (1–2 tuần tới)                                                                                                                    |
| :------------------------------------------- | :--------------------------------------- | :------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Thầy Nguyễn Tuấn Anh** _(Mentor)_       | **Champion**<br>🟢 _Ủng hộ mạnh_         | Mô hình chạy có ổn định không, có bị trả lời bịa đặt (hallucination) về dị ứng không.             | **Thuận lợi:** Hướng dẫn kỹ thuật và có thể giới thiệu cho nhóm 1 trường quen để chạy thử.                     | Gửi thầy xem kết quả test thực tế và video demo quét món ăn trước 18h thứ Năm (04/09), xin lịch gặp 30 phút để nhờ thầy kết nối trường thử nghiệm.       |
| **2. Chú Nguyễn Văn Bình** _(Bếp trưởng)_    | **Supporter**<br>🟢 _Ủng hộ_             | Phần mềm có dễ dùng không, có giúp chú đỡ phải bấm máy tính 2–3 tiếng mỗi cuối tuần không.        | **Thuận lợi:** Cung cấp thực đơn cũ thực tế và góp ý xem món AI gợi ý có nấu được thật không.                  | Đến gặp trực tiếp chú Bình tại bếp ăn trường vào chiều thứ Ba (02/09), xin file thực đơn cũ 3 tháng qua và quan sát cách chú đang lên món.               |
| **3. Cô Hoàng Lan** _(Hiệu trưởng)_          | **Blocker**<br>⚠️ _Đang e ngại_          | Trách nhiệm an toàn cho học sinh. Sợ phần mềm sót dị ứng làm trẻ nhập viện thì trường mất uy tín. | **Trở ngại:** Có thể từ chối ngay từ đầu nếu nghĩ nhóm để AI tự quyết định thay người.                         | Viết 1 bản cam kết ngắn gọn: "AI chỉ đóng vai trò trợ lý nhắc nhở, quyền duyệt cuối luôn là chữ ký của Bếp trưởng và Y tế", gửi cô xem trước ngày 08/09. |
| **4. Chị Lê Mai Anh** _(Đại diện Phụ huynh)_ | **Supporter / Blocker**<br>🟡 _Khắt khe_ | Nguồn số liệu dinh dưỡng lấy từ đâu; liệu thức ăn có thật sự sạch và an toàn cho con mình không.  | **Trở ngại:** Có thể phản đối trong buổi họp phụ huynh nếu nghĩ trường dùng phần mềm linh tinh chưa kiểm định. | Gửi bảng tóm tắt chứng minh dữ liệu nhóm dùng lấy từ Viện Dinh Dưỡng và mời chị xem thử chức năng quét dị ứng vào sáng thứ Bảy (06/09).                  |

---

### 🚦 GATE 1: Kiểm tra bản đồ Stakeholder

| Tiêu chí                                                   | Đánh giá | Chi tiết                                          |
| :--------------------------------------------------------- | :------: | :------------------------------------------------ |
| Có đủ ít nhất 6 người liên quan cụ thể?                    |  ✅ Đạt  | 7 người cụ thể với tên, vị trí rõ ràng            |
| Đặt đúng vị trí trên 4 góc ma trận?                        |  ✅ Đạt  | Đủ 4 góc: Champion, Blocker, Supporter, Bystander |
| Có đánh giá thái độ thực tế (Ủng hộ / Trung lập / E ngại)? |  ✅ Đạt  | Thể hiện đúng nỗi lo thực tế của từng người       |
| Có việc cần làm cụ thể kèm thời hạn cho 4 người ưu tiên?   |  ✅ Đạt  | Đều có ngày giờ, đầu việc rõ ràng trong 1–2 tuần  |

---

## 🎯 Phase 2: Trình bày "Kết luận trước" & Ma trận Phân quyền RACI (Trang 2 / 4 PDF)

### 1. Bản Pitch ngắn gửi Cô Hiệu trưởng (Người cần thuyết phục nhất)

_Mục tiêu:_ Thuyết phục Ban Giám hiệu cho nhóm thử nghiệm chạy song song tại trường trong 2 tuần mà không làm xáo trộn việc nấu nướng hiện tại.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        BẢN ĐỀ XUẤT NGẮN GỌN (KẾT LUẬN TRƯỚC)                           │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [1. ĐỀ XUẤT CHÍNH - NÓI NGAY KẾT LUẬN]                                                 │
│ Nhóm đề xuất trường cho phép chạy thử nghiệm song song NutriMenu AI trong 2 tuần:      │
│ Hệ thống giúp phát hiện 100% món ăn chứa thành phần dị ứng ẩn và giảm 80% thời gian    │
│ tính toán thực đơn, mà KHÔNG làm thay đổi bất kỳ quy trình nấu nướng nào của trường.   │
│                                                                                        │
│ [2. VÌ SAO NHÀ TRƯỜNG NÊN QUAN TÂM?]                                                   │
│ • Tránh rủi ro học sinh bị dị ứng: Trẻ nhỏ rất nhạy cảm, chỉ cần một chút bột đậu phộng│
│   hoặc gluten ẩn trong nước sốt có thể làm học sinh bị ngứa, khó thở.                  │
│ • Đúng chuẩn dinh dưỡng Bộ Y tế: Tự động tính đúng mức calo, đạm, béo cho lứa tuổi 6–11,│
│   Bếp trưởng không còn phải cộng trừ thủ công dễ nhầm lẫn.                             │
│ • Minh bạch với Phụ huynh: Cuối tuần xuất bảng dinh dưỡng rõ ràng gửi phụ huynh, giúp  │
│   phụ huynh yên tâm tuyệt đối khi gửi con ăn bán trú.                                  │
│                                                                                        │
│ [3. DỮ LIỆU & BẰNG CHỨNG THỰC TẾ]                                                      │
│ • Nhóm đã chạy thử nghiệm trên 50 bộ thực đơn tuần thực tế: AI nhận diện đúng 100%     │
│   các món có chất gây dị ứng (không bỏ sót trường hợp nào trong 200 món thử nghiệm).   │
│ • Tính toán calo lệch dưới 4.2% so với số liệu đối chiếu của Viện Dinh Dưỡng.          │
│ • Tốc độ xử lý: Đọc và kiểm tra cả tuần thực đơn chỉ mất 3.5 giây thay vì 3 tiếng.     │
│                                                                                        │
│ [4. ĐỀ NGHỊ MỘT BƯỚC ĐI NHỎ TIẾP THEO]                                                 │
│ Nhóm xin phép được gặp cô và chú Bếp trưởng 15 phút vào sáng thứ Tư (03/09) để chiếu   │
│ thử phần mềm chạy ngay trên chính thực đơn tuần tới của trường.                        │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2. Chuẩn bị câu trả lời khi bị phản biện

- **Câu hỏi phản biện khó nhất từ Hiệu trưởng:**

  > _"Nếu phần mềm nhận diện sai hoặc bỏ sót chất gây dị ứng làm học sinh nhập viện, ai là người chịu trách nhiệm trước phụ huynh và pháp luật? Trường không thể mạo hiểm."_

- **Cách nhóm xử lý dựa trên nguyên tắc an toàn thực tế:**
  1. **Người duyệt cuối vẫn là con người:** NutriMenu AI chỉ là công cụ hỗ trợ rà soát trước. Quyết định chốt thực đơn và ký tên chịu trách nhiệm vẫn là Bếp trưởng và Cán bộ Y tế.
  2. **Cơ chế an toàn (Không chắc chắn thì báo kiểm tra lại):** Nếu gặp món lạ, tên viết tắt hoặc độ tin cậy dưới 95%, hệ thống sẽ **báo đỏ yêu cầu Bếp trưởng kiểm tra lại bằng tay**, tuyệt đối không tự ý báo an toàn.
  3. **Chạy song song không rủi ro:** Trong 2 tuần thử nghiệm, trường vẫn nấu theo quy trình bình thường, phần mềm chỉ chạy ngầm để so sánh kết quả.

---

### 3. Thống nhất góc nhìn giữa các thành viên

- **Đỗ Tú Anh (Quản lý):** Nhìn từ góc độ quản trị rủi ro và sự an tâm của phụ huynh/nhà trường.
- **Trần Thanh Huyền (Kỹ sư AI):** Nhìn từ độ chính xác của thuật toán và các con số kiểm thử.
- **Thiều Thị Ngọc Ánh (Kỹ sư Dữ liệu):** Nhìn từ sự tiện lợi cho bếp ăn và nguồn số liệu chuẩn từ Viện Dinh Dưỡng.
- $\rightarrow$ **Cả nhóm chốt:** Bản pitch đưa thẳng vấn đề an toàn cho học sinh lên đầu, sau đó chứng minh bằng số liệu test thực tế.

---

### 4. Ma trận Phân quyền Công việc (RACI Matrix)

_Quy ước:_

- **R (Responsible):** Người trực tiếp làm việc.
- **A (Accountable):** Người chịu trách nhiệm cuối cùng (**Mỗi việc chỉ có 1 người giữ chữ A**).
- **C (Consulted):** Người được hỏi ý kiến chuyên môn trước khi làm.
- **I (Informed):** Người được thông báo sau khi hoàn thành.

|  STT  | Công việc chính (1–2 tháng tới)                           | Đỗ Tú Anh<br>_(Trưởng nhóm / PO)_ | Trần Thanh Huyền<br>_(Kỹ sư AI)_ | Thiều Thị Ngọc Ánh<br>_(Dữ liệu & Backend)_ | Bếp trưởng & Y tế<br>_(Người dùng trực tiếp)_ | Bác sĩ Dinh dưỡng<br>_(Chuyên gia tư vấn)_ |
| :---: | :-------------------------------------------------------- | :-------------------------------: | :------------------------------: | :-----------------------------------------: | :-------------------------------------------: | :----------------------------------------: |
| **1** | **Xử lý và nhập bảng số liệu dinh dưỡng & dị ứng**        |                 I                 |                C                 |                  **A / R**                  |                       C                       |                     C                      |
| **2** | **Xây dựng mô hình AI nhận diện món và bắt dị ứng**       |                 I                 |            **A / R**             |                      C                      |                       I                       |                     I                      |
| **3** | **Làm giao diện web và API cho người dùng nhập thực đơn** |                 C                 |                C                 |                  **A / R**                  |                       C                       |                     I                      |
| **4** | **Chạy bộ kiểm thử đo độ chính xác của AI**               |                 C                 |              **A**               |                      R                      |                       I                       |                     C                      |
| **5** | **Mang phần mềm đi chạy thử thực tế tại bếp ăn trường**   |             **A / R**             |                C                 |                      C                      |                       C                       |                     I                      |
| **6** | **Quyết định cho phép ra mắt bản chính thức**             |               **A**               |                C                 |                      C                      |                       I                       |                     I                      |

_Lưu ý rõ ràng:_ Ở phần kiểm thử (việc 4), Huyền chịu trách nhiệm chất lượng AI (`A`), nhưng Ánh là người trực tiếp chạy kịch bản test (`R`) để đảm bảo khách quan. Việc quyết định ra mắt (việc 6) do Tú Anh chịu trách nhiệm cuối cùng (`A`).

---

### 🚦 GATE 2: Kiểm tra Pitch & RACI

| Tiêu chí                                           | Đánh giá | Chi tiết                                                   |
| :------------------------------------------------- | :------: | :--------------------------------------------------------- |
| Pitch có nói kết luận trước không?                 |  ✅ Đạt  | Đưa ngay đề xuất thử nghiệm 2 tuần, phát hiện 100% dị ứng  |
| Có số liệu chứng minh và lời đề nghị nhỏ rõ ràng?  |  ✅ Đạt  | Có số liệu 50 thực đơn, 3.5 giây xử lý và hẹn gặp 15 phút  |
| Có kịch bản phản biện và cách giải quyết an toàn?  |  ✅ Đạt  | Xử lý triệt để nỗi lo pháp lý bằng cơ chế người duyệt cuối |
| RACI có đủ việc quan trọng, mỗi dòng đúng 1 chữ A? |  ✅ Đạt  | 6 việc rõ ràng, không ai bị chồng chéo quyền quyết định    |

---

## 🏗️ Phase 3: Thiết Kế Đội Ngũ AI & Bổ Sung Năng Lực (Trang 3 / 4 PDF)

### 1. Chọn Mô hình Tổ chức Nhóm (AI Team Architecture)

- **Mô hình chọn:** **Embedded (Mô hình Nhúng trực tiếp vào sản phẩm)**
- **Lý do:**
  - Nhóm chỉ có 3 người và đang tập trung làm duy nhất một sản phẩm từ đầu (từ con số 0 lên MVP).
  - Cả 3 người ngồi cùng nhau, trao đổi trực tiếp mỗi ngày, nắm rõ phản hồi của bếp ăn để sửa code ngay mà không cần qua các khâu trung gian phức tạp.

```mermaid
graph TD
    subgraph Nhóm NutriMenu AI (Mô hình Nhúng)
        PO["Đỗ Tú Anh<br/>Trưởng nhóm & Quản lý"] --- AI["Trần Thanh Huyền<br/>Kỹ sư AI"]
        AI --- BE["Thiều Thị Ngọc Ánh<br/>Kỹ sư Dữ liệu & Backend"]
        BE --- PO
    end
    Nhóm --> Pilot["Chạy thử trực tiếp tại Bếp ăn trường"]
    Advisor["Bác sĩ Viện Dinh Dưỡng (Hợp tác tư vấn)"] -. Góp ý chuyên môn .-> Nhóm
```

---

### 2. Vai trò Hiện tại & Vai trò Cần thêm khi Mở rộng

#### A. Vai trò cốt lõi (3 thành viên hiện tại đang làm):

1. **Quản lý Sản phẩm (Đỗ Tú Anh):** Đi thực tế nói chuyện với trường học, lên danh sách tính năng cần làm, theo dõi hạn chót.
2. **Kỹ sư AI (Trần Thanh Huyền):** Viết logic prompt, kết nối cơ sở dữ liệu món ăn, thiết lập luật chặn lỗi nhận diện dị ứng.
3. **Kỹ sư Dữ liệu & Backend (Thiều Thị Ngọc Ánh):** Dọn dẹp dữ liệu dinh dưỡng, viết API kết nối và chuẩn bị các bài test lỗi.

#### B. Vai trò mở rộng (Chỉ cần khi đã có 10+ trường sử dụng):

1. **Kỹ sư Vận hành AI (MLOps):** Giám sát tốc độ phản hồi và chi phí gọi AI khi lượng người dùng tăng cao.
2. **Chuyên viên Pháp chế:** Rà soát hợp đồng và cam kết an toàn thông tin với các trường học.

---

### 3. Cách Bổ sung Năng lực còn thiếu (Priority Resourcing)

Thay vì tuyển ồ ạt tốn kém, nhóm chọn cách bổ sung thông minh cho 3 điểm còn thiếu:

|  STT  | Năng lực nhóm đang thiếu                                                                |             Cách giải quyết _(Tuyển / Thuê ngoài / Hợp tác)_              | Lý do chọn cách này                                                                                                                                                                          | Thời điểm cần                                       |
| :---: | :-------------------------------------------------------------------------------------- | :-----------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------- |
| **1** | **Kiến thức sâu về Dinh dưỡng Nhi khoa**<br>_(Các trường hợp dị ứng chéo phức tạp)_     |           🤝 **HỢP TÁC (Partner)**<br>_(Nhờ chuyên gia cố vấn)_           | Giai đoạn làm thử nghiệm chỉ cần bác sĩ xem qua bộ luật và thực đơn khó, **không cần tuyển người làm toàn thời gian**. Hợp tác với bác sĩ Viện Dinh Dưỡng giúp tăng độ tin cậy cho sản phẩm. | **Ngay tuần 1** _(Trước khi hoàn thiện dữ liệu)_    |
| **2** | **Thiết kế Giao diện Web cho Bếp trưởng**<br>_(Cần màn hình to, chữ rõ, dễ bấm)_        |   💼 **THUÊ NGOÀI (Outsource)**<br>_(Thuê thiết kế giao diện ngắn hạn)_   | Nhóm chỉ cần khoảng 8 màn hình cơ bản cho bản chạy thử. Thuê bạn thiết kế tự do (Freelancer) làm trọn gói trong 1 tuần sẽ nhanh và tiết kiệm hơn nhiều.                                      | **Tuần 2–3** _(Trước khi mang đi demo ở trường)_    |
| **3** | **Bộ công cụ Tự động Chấm điểm AI**<br>_(Chạy test tự động xem AI có bị sót lỗi không)_ | 🎯 **TỰ HỌC NỘI BỘ (Internal Upskill)**<br>_(Nâng cao tay nghề của nhóm)_ | Đây là kỹ thuật cốt lõi của nhóm để đảm bảo an toàn. Bạn Huyền (Kỹ sư AI) sẽ tự nghiên cứu các thư viện mã nguồn mở để dựng bộ test tự động cho nhóm.                                        | **Tháng thứ 2** _(Trước khi mở rộng sang 3 trường)_ |

---

### 4. Mục tiêu Chung của Nhóm (Squad Goal)

> _"Nhóm chúng tôi làm chủ **công nghệ AI kết hợp với dữ liệu dinh dưỡng chuẩn**, chịu trách nhiệm đưa **việc kiểm tra thực đơn bán trú từ chỗ làm tay mất 3 tiếng với nhiều rủi ro thành một hệ thống tự động kiểm tra chỉ mất dưới 5 giây và phát hiện chính xác 100% các thành phần dị ứng**."_

---

### 🚦 GATE 3: Kiểm tra Thiết kế Nhóm

| Tiêu chí                                                        | Đánh giá | Chi tiết                                             |
| :-------------------------------------------------------------- | :------: | :--------------------------------------------------- |
| Chọn mô hình nhóm rõ ràng có giải thích?                        |  ✅ Đạt  | Mô hình Embedded phù hợp cho nhóm 3 người làm nhanh  |
| Phân rõ vai trò hiện tại và vai trò khi mở rộng?                |  ✅ Đạt  | 3 vai trò thực tế + 2 vai trò chuẩn bị cho tương lai |
| Chọn đúng cách bù đắp năng lực thiếu (Thuê / Hợp tác / Tự học)? |  ✅ Đạt  | Hợp tác bác sĩ, thuê ngoài UI, tự học bộ test AI     |
| Mục tiêu nhóm rõ ràng, nói được sự thay đổi cụ thể?             |  ✅ Đạt  | Từ làm tay 3 tiếng $\rightarrow$ tự động dưới 5 giây |

---

## 📈 Phase 4: Sức Khỏe Đội Ngũ & Kế Hoạch 30 Ngày (Trang 4 / 4 PDF)

### 1. Nhóm Tự Đánh Giá Sức Khỏe Vận Hành (Thang điểm 1–5)

Từng thành viên tự chấm điểm độc lập:

| Khía cạnh đánh giá                                                          | Đỗ Tú Anh<br>_(Quản lý)_ | Trần Thanh Huyền<br>_(Kỹ sư AI)_ | Thiều Thị Ngọc Ánh<br>_(Kỹ sư Dữ liệu)_ | Điểm trung bình |              Nhận xét thực tế              |
| :-------------------------------------------------------------------------- | :----------------------: | :------------------------------: | :-------------------------------------: | :-------------: | :----------------------------------------: |
| **1. Chất lượng AI**<br>_(Đầu ra đúng, không bị bịa thông tin)_             |          3 / 5           |              3 / 5               |                  4 / 5                  |   **3.3 / 5**   |  🟡 Khá ổn nhưng chưa có bộ test tự động   |
| **2. Tiến độ công việc**<br>_(Làm đúng hẹn cam kết)_                        |          4 / 5           |              3 / 5               |                  3 / 5                  |   **3.3 / 5**   |      🟡 Cơ bản đúng hạn nhưng hơi gấp      |
| **3. Tinh thần đồng đội**<br>_(Trao đổi thẳng thắn, hỗ trợ nhau)_           |          4 / 5           |              4 / 5               |                  5 / 5                  |   **4.3 / 5**   |     🟢 Rất tốt, mọi người hiểu ý nhau      |
| **4. Tốc độ ra sản phẩm**<br>_(Thời gian từ lúc sửa code đến lúc thử được)_ |          3 / 5           |              2 / 5               |                  3 / 5                  |   **2.7 / 5**   | 🔴 **Thấp nhất (Điểm nghẽn cần sửa ngay)** |

---

### 2. Chỉ ra Vấn đề Lớn Nhất Cần Sửa

- **Khía cạnh điểm thấp nhất:** **Tốc độ ra sản phẩm (2.7 / 5)**.
- **Nguyên nhân chênh lệch:** Bạn Huyền chấm điểm AI là 3 vì lo lắng chưa có bộ đo tự động, trong khi bạn Ánh thấy các mẫu thử cơ bản chạy tốt nên chấm 4.
- **Vấn đề cốt lõi cần giải quyết ngay trong tháng tới:**
  > **"Mỗi lần chỉnh sửa prompt hoặc cập nhật dữ liệu món ăn, nhóm phải ngồi kiểm tra lại bằng tay từng món mất cả buổi chiều."** Việc này làm tốc độ làm việc bị chậm lại và dễ bỏ sót lỗi khi đem đi demo cho trường học.

---

### 3. Nâng cấp Năng lực Thành viên (Khung L1 $\rightarrow$ L3)

- **L1 — Hiểu và dùng cơ bản:** Biết dùng các công cụ AI có sẵn.
- **L2 — Ứng dụng thực tế:** Biết gọi API, viết prompt tốt, làm hệ thống RAG cơ bản.
- **L3 — Xây dựng nâng cao:** Tự làm bộ đo đạc kiểm thử tự động, tối ưu mô hình, làm chủ hệ thống an toàn.

| Thành viên                           |                Trình độ hiện tại                 | Năng lực cần nâng cấp tiếp theo                                                                                        | Việc cụ thể làm trong 30 ngày                                                                                                           |
| :----------------------------------- | :----------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| **Trần Thanh Huyền**<br>_(Kỹ sư AI)_ | **L2 (Ứng dụng)**<br>_(Đã làm tốt RAG & Prompt)_ | 🚀 **Tiến lên L3 (Xây dựng nâng cao):**<br>Làm chủ kỹ thuật **Tự động đo lường chất lượng AI** để không phải test tay. | Soạn bộ **50 bài kiểm tra mẫu** (gồm các ca món ăn có thành phần dị ứng phức tạp), viết script tự động chạy chấm điểm mỗi khi sửa code. |

---

### 4. Kế hoạch Hành động Cụ thể trong 30 Ngày Tới

|  STT  | Vấn đề cần xử lý                                                 | Hành động cụ thể (Làm gì?)                                                                                           |                 Người phụ trách                 |                    Hạn chót                     | Dấu hiệu hoàn thành (Kết quả nhìn thấy)                                                                                         |
| :---: | :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------: | :---------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------ |
| **1** | Mất nhiều thời gian test tay, không biết AI có bị sót lỗi không. | Lập bộ 50 bài test mẫu và viết code `eval_pipeline.py` tự động đo tỷ lệ bắt đúng dị ứng.                             |      **Trần Thanh Huyền**<br>_(Kỹ sư AI)_       |                 **10/09/2026**                  | Chạy code tự động xuất ra file kết quả `eval_report.json` với **tỷ lệ bắt đúng dị ứng $\ge 99\%$**, không bị lỗi văng ứng dụng. |
| **2** | Dữ liệu món ăn còn lưu ở file Excel rời, chưa có API kết nối.    | Nhập 500 thành phần thực phẩm chuẩn vào cơ sở dữ liệu, viết 3 API chính (quét dị ứng, tính calo, gợi ý món đổi).     | **Thiều Thị Ngọc Ánh**<br>_(Dữ liệu & Backend)_ |                 **15/09/2026**                  | Chạy kiểm tra API phản hồi nhanh dưới 0.8 giây, có tài liệu hướng dẫn dùng API rõ ràng.                                         |
| **3** | Sợ làm tính năng không đúng thực tế bếp ăn cần.                  | Lên lịch họp cố định 30 phút vào mỗi chiều thứ Sáu để nhóm tự soi lỗi và lấy góp ý của chú Bếp trưởng trên bản demo. |        **Đỗ Tú Anh**<br>_(Trưởng nhóm)_         | **Bắt đầu từ 05/09/2026**<br>_(Làm đều 4 tuần)_ | Có đủ 4 biên bản ghi nhận góp ý của người dùng để chỉnh sửa cho tuần sau.                                                       |

---

### 🚦 GATE 4: Kiểm tra Kế hoạch 30 ngày

| Tiêu chí                                                    | Đánh giá | Chi tiết                                                 |
| :---------------------------------------------------------- | :------: | :------------------------------------------------------- |
| Chấm điểm đủ 4 phần sức khỏe của nhóm?                      |  ✅ Đạt  | Có điểm từng người và điểm trung bình rõ ràng            |
| Tìm ra đúng điểm nghẽn lớn nhất?                            |  ✅ Đạt  | Tốc độ chậm do phải kiểm tra thủ công bằng tay           |
| Chọn 1 người và nâng cấp năng lực rõ ràng?                  |  ✅ Đạt  | Bạn Huyền nâng từ L2 lên L3 qua việc làm bộ test tự động |
| 3 hành động có đủ Người làm + Hạn chót + Kết quả nhìn thấy? |  ✅ Đạt  | Cả 3 việc đều cụ thể, đo đếm được                        |

---

## 🔍 Phase 5: Tự Soi Lỗi, Tính Nhất Quán & Hoàn Thiện Hồ Sơ Nộp

### 1. Bảng Kiểm Tra Tính Khớp Nối Giữa Các Trang

| So sánh giữa các phần                                                            | Điểm cần kiểm tra                                                            | Thực tế bài làm của nhóm                                                                                                                                                                                                   |        Kết quả        |
| :------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------: |
| **Trang 1 $\leftrightarrow$ Trang 2** _(Bên liên quan vs Bài Pitch/RACI)_        | Người e ngại nhất ở Trang 1 có phải là người nhận bản Pitch ở Trang 2 không? | Đúng: **Cô Hiệu trưởng (người lo lắng rủi ro ở Trang 1)** là người nhận bản đề xuất ở Trang 2. Bếp trưởng và Bác sĩ dinh dưỡng đều có mặt trong bảng phân quyền RACI.                                                      | ✅ **Hoàn toàn khớp** |
| **Trang 3 $\leftrightarrow$ Trang 4** _(Năng lực còn thiếu vs Kế hoạch 30 ngày)_ | Năng lực nhóm thiếu ở Trang 3 có được giải quyết ở Trang 4 không?            | Đúng: Năng lực thiếu số 3 (_Bộ kiểm tra AI tự động_) được giải quyết bằng việc nâng cấp năng lực cho bạn Huyền và việc làm số 1 trong kế hoạch 30 ngày.                                                                    | ✅ **Hoàn toàn khớp** |
| **Trang 2 $\leftrightarrow$ Trang 4** _(Bảng RACI vs Người phụ trách hành động)_ | Người làm hành động 30 ngày có đúng vai trò trong bảng RACI không?           | Đúng: <br>• Việc 1 (Test AI) do **Huyền** làm (người chịu trách nhiệm AI).<br>• Việc 2 (Dữ liệu/API) do **Ánh** làm (người chịu trách nhiệm Backend).<br>• Việc 3 (Lấy ý kiến người dùng) do **Tú Anh** làm (Trưởng nhóm). | ✅ **Hoàn toàn khớp** |

---

### 2. Danh mục Hồ sơ Nộp Bài

- **Link GitHub Repository:** `https://github.com/anhdotu0912/Track1_Day27_Team68_DuAn68`
- **File PDF Nộp Kèm:** `Day27_AI-Team-Lab_Team68.pdf` (Đúng chuẩn 4 trang):
  - **Trang 1:** Bản đồ 7 bên liên quan, phân loại 4 nhóm và kế hoạch hành động 1–2 tuần tới.
  - **Trang 2:** Đề xuất "Kết luận trước" gửi Hiệu trưởng, cách trả lời phản biện và Bảng phân quyền RACI 6 việc.
  - **Trang 3:** Cấu trúc nhóm Embedded, phân chia vai trò, cách bù đắp năng lực thiếu và Mục tiêu chung của nhóm.
  - **Trang 4:** Điểm tự đánh giá sức khỏe nhóm, nâng cấp kỹ sư AI từ L2 lên L3 và 3 việc cụ thể trong 30 ngày.

---

### 🚦 GATE 5: Kiểm tra Sẵn sàng Nộp bài

| Tiêu chí                                                                  | Đánh giá | Chi tiết                                       |
| :------------------------------------------------------------------------ | :------: | :--------------------------------------------- |
| File README.md đầy đủ, văn phong tự nhiên, thực tế?                       |  ✅ Đạt  | Đầy đủ từ Phase 0 đến Phase 5, rõ ràng, dễ đọc |
| Chuẩn bị file PDF đúng tên `Day27_AI-Team-Lab_Team68.pdf` tối đa 4 trang? |  ✅ Đạt  | Nội dung chia gọn gàng tương ứng 4 trang       |
| Toàn bộ bài làm có tính nhất quán từ đầu đến cuối?                        |  ✅ Đạt  | Người, việc và mục tiêu liên kết chặt chẽ      |
| Link repository truy cập bình thường?                                     |  ✅ Đạt  | Repo public trên GitHub                        |

---
