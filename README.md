# Track 1 - Day 27 — AI Team Lab

- **Team:** Team 68
- **Thành viên (3–5 người):**
  1. **Đỗ Tú Anh** — MSSV: `2A202601272` _(Trưởng nhóm / Product Owner)_
  2. **Trần Thanh Huyền** — MSSV: `2A202601578` _(Lead AI Engineer)_
  3. **Thiều Thị Ngọc Ánh** — MSSV: `2A202601864` _(Backend, Data & QA Specialist)_
- **Tên dự án:** **NutriMenu AI** — Hệ thống AI Thẩm định Dinh dưỡng & Cảnh báo Dị ứng Thực đơn Bán trú
- **Link sản phẩm/demo (nếu có):** `https://github.com/anhdotu0912/Track1_Day27_Team68_DuAn68`

---

## 📌 Phase 0: Chốt Phạm vi & Cách làm (Scope & Ground Rules)

### 1. Thông tin Đội ngũ (Team 68)

- **Quy mô:** 3 thành viên.
- **Danh sách thành viên & Phân công vai trò:**
  1. **Đỗ Tú Anh** (MSSV: `2A202601272`) — _Trưởng nhóm (Team Lead) & Product Owner_ (Chịu trách nhiệm tổng hợp bài nộp, quản lý GitHub repository và điều phối chung).
  2. **Trần Thanh Huyền** (MSSV: `2A202601578`) — _Lead AI / LLM Engineer_ (Chịu trách nhiệm thiết kế AI Pipeline, Prompt Orchestration, AI Guardrails và Benchmark độ chính xác).
  3. **Thiều Thị Ngọc Ánh** (MSSV: `2A202601864`) — _Backend, Data & Domain QA Specialist_ (Chịu trách nhiệm chuẩn hóa bộ dữ liệu dinh dưỡng Viện Dinh Dưỡng Quốc Gia, tích hợp Backend API và kiểm thử an toàn dị ứng).

---

### 2. Định nghĩa Dự án & Bài toán

- **Tên dự án:** **NutriMenu AI**
- **Lĩnh vực:** EdTech / HealthTech / Food Safety.
- **Mô tả bài toán:** Bếp ăn các trường mầm non & tiểu học bán trú phải lên thực đơn hàng tuần phục vụ hàng trăm học sinh. Tuy nhiên, việc tính toán cân đối vi chất (Calo, Đạm, Đường, Béo, Canxi, Sắt) theo độ tuổi rất tốn thời gian, và đặc biệt là rủi ro bỏ sót **thành phần gây dị ứng** (đậu phộng, hải sản, gluten, trứng, sữa...) có thể gây sốc phản vệ nguy hiểm.
- **Giải pháp NutriMenu AI:** Ứng dụng AI (RAG + Rule-based Guardrails) để tự động đọc thực đơn tuần, đối chiếu bảng thành phần thực phẩm của Viện Dinh Dưỡng Quốc Gia, cảnh báo dị ứng tức thì và gợi ý món thay thế tương đương dinh dưỡng.

---

### 3. Mục tiêu Cốt lõi Trong 1–3 Tháng tới (Current Milestone)

- **Milestone 1 (Tháng 1):** Xây dựng MVP phân tích file thực đơn (PDF/Excel), nhận diện 100% các nhóm dị ứng nguy hiểm phổ biến theo chuẩn BYT/FDA.
- **Milestone 2 (Tháng 2):** Đối soát ma trận dinh dưỡng theo lứa tuổi (Mầm non: 3–5 tuổi; Tiểu học: 6–11 tuổi) với độ lệch calo & vi chất $< 5\%$.
- **Milestone 3 (Tháng 3):** Thử nghiệm Pilot tại 03 trường tiểu học bán trú đối tác, giảm $80\%$ thời gian duyệt thực đơn của Ban Giám hiệu và Bếp trưởng.

---

### 4. Công cụ & Định dạng Bài làm

- **Format bài nộp:**
  - `README.md` hoàn chỉnh trên GitHub repo: `Track1_Day27_Team68_DuAn68`.
  - `01 File PDF (tối đa 4 trang)` xuất từ Google Slides/Docs chứa trọn vẹn 4 Artefact.
- **Người tổng hợp & Quản trị Repo:** Đỗ Tú Anh.

---

### 🚦 GATE 0 CHECK: Scope đã rõ ràng

| Tiêu chí                                      | Trạng thái | Ghi chú                                                |
| :-------------------------------------------- | :--------: | :----------------------------------------------------- |
| Cả team thống nhất cùng một bài toán dự án AI |   ✅ Đạt   | Dự án NutriMenu AI                                     |
| Mục tiêu 1–3 tháng cụ thể, đo lường được      |   ✅ Đạt   | MVP dị ứng 100%, sai số dinh dưỡng <5%, pilot 3 trường |
| Đã phân công Trưởng nhóm & người tổng hợp     |   ✅ Đạt   | Đỗ Tú Anh phụ trách repo & nộp bài                     |
| Số lượng thành viên hợp lệ                    |   ✅ Đạt   | 3 thành viên                                           |

---

## 🗺️ Phase 1: Stakeholder Map & Chiến lược Tiếp cận (Trang 1 / 4 PDF)

### 1. Danh sách 7 Stakeholder Cụ thể của Dự án NutriMenu AI

1. **Cô Hoàng Lan — Hiệu trưởng Trường Tiểu học Bán trú (Đơn vị Pilot tiềm năng):** Người có thẩm quyền cao nhất phê duyệt áp dụng phần mềm vào quy trình vận hành bữa ăn của trường.
2. **Chú Nguyễn Văn Bình — Bếp trưởng Bếp ăn Bán trú (800 suất ăn/ngày):** Người trực tiếp lên thực đơn tuần, định lượng nguyên liệu và chịu trách nhiệm chế biến.
3. **TS. BS. Vũ Thu Trang — Chuyên gia Dinh dưỡng Nhi (Viện Dinh Dưỡng Quốc Gia):** Cố vấn chuyên môn về nhu cầu khuyến nghị dinh dưỡng (RNI) cho trẻ em Việt Nam.
4. **Chị Lê Mai Anh — Trưởng Ban đại diện Cha mẹ học sinh (Phụ huynh có con dị ứng đậu phộng nặng):** Đại diện tiếng nói phụ huynh, giám sát an toàn suất ăn học đường.
5. **Y sĩ Trần Quốc Bảo — Cán bộ Y tế Học đường:** Người quản lý hồ sơ bệnh án dị ứng của học sinh và trực tiếp xử lý y tế khi có sự cố tại trường.
6. **Thầy Nguyễn Tuấn Anh — Giảng viên / Mentor Hướng dẫn AI:** Đánh giá độ tin cậy kỹ thuật (RAG accuracy, hallucination rate) và kết nối mạng lưới pilot.
7. **Anh Đặng Quốc Cường — Giám đốc Công ty Suất ăn Công nghiệp GreenCatering:** Đơn vị ký hợp đồng thầu nấu ăn cho 5 trường tiểu học trên địa bàn.

---

### 2. Stakeholder Map Matrix (Influence × Interest & Stance)

```
                       Interest (Mức độ quan tâm)
                     THẤP ───────────────────► CAO
        ┌─────────────────────────────┬─────────────────────────────┐
        │ [BLOCKER / CẦN THUYẾT PHỤC] │ [CHAMPION / ỦNG HỘ CHỦ CHỐT]│
     C  │                             │                             │
     A  │ • Cô Hoàng Lan (Hiệu trưởng)│ • Thầy Nguyễn Tuấn Anh      │
     O  │   Stance: ⚠️ Chưa ủng hộ     │   (Mentor hướng dẫn)        │
        │   (E ngại rủi ro an toàn)   │   Stance: 🟢 Ủng hộ mạnh    │
I       │                             │ • TS. BS. Vũ Thu Trang      │
n       │                             │   (Viện Dinh Dưỡng)         │
f       │                             │   Stance: 🟢 Ủng hộ         │
l       ├─────────────────────────────┼─────────────────────────────┤
u       │ [BYSTANDER / THEO DÕI]      │ [SUPPORTER / ỦNG HỘ-GÓP Ý]  │
e       │                             │                             │
n       │ • Anh Đặng Quốc Cường       │ • Chú Nguyễn Văn Bình       │
c       │   (Giám đốc GreenCatering)  │   (Bếp trưởng)              │
e       │   Stance: ⚪ Trung lập       │   Stance: 🟢 Ủng hộ         │
        │                             │ • Chị Lê Mai Anh (Phụ huynh)│
     T  │                             │   Stance: 🟡 Trung lập      │
     H  │                             │ • Y sĩ Trần Quốc Bảo (Y tế) │
     Ấ  │                             │   Stance: 🟢 Ủng hộ         │
     P  │                             │                             │
        └─────────────────────────────┴─────────────────────────────┘
```

#### Phân tích Stance & Quadrant:

- **Champion (Influence Cao, Interest Cao):** Thầy Mentor Nguyễn Tuấn Anh & TS. BS. Vũ Thu Trang — Có ảnh hưởng lớn về định hướng giải pháp và uy tín học thuật, rất quan tâm đến ứng dụng AI chuẩn hóa dinh dưỡng học đường.
- **Blocker (Influence Cao, Interest Thấp đến Trung bình):** Cô Hoàng Lan (Hiệu trưởng) — Giữ quyền quyết định cho phép pilot nhưng e ngại rủi ro trách nhiệm pháp lý nếu AI tư vấn sai gây dị ứng/ngộ độc cho học sinh.
- **Supporter (Influence Thấp, Interest Cao):** Chú Nguyễn Văn Bình (Bếp trưởng) và Y sĩ Trần Quốc Bảo — Hưởng lợi trực tiếp giúp giảm tải công việc tính toán thực đơn; Chị Lê Mai Anh (Phụ huynh) quan tâm cao đến sức khỏe con cái nhưng cần kiểm chứng tính minh bạch dữ liệu.
- **Bystander (Influence Thấp, Interest Thấp):** Anh Đặng Quốc Cường (Giám đốc bên thứ 3) — Đứng ngoài quan sát, chỉ quan tâm khi nhà trường chính thức yêu cầu bắt buộc áp dụng tool.

---

### 3. Chiến lược Hành động cho 4 Stakeholder Ưu tiên (1–2 Tuần tới)

| Stakeholder                                  | Phân loại & Stance                                         | Họ quan tâm điều gì?                                                                                                     | Giúp / Cản trở dự án thế nào?                                                                                               | Hành động cụ thể (Actionable Plan)                                                                                                                                                                                            |
| :------------------------------------------- | :--------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Thầy Nguyễn Tuấn Anh** _(Mentor AI)_    | **Champion**<br>🟢 _Ủng hộ mạnh_                           | Độ tin cậy của mô hình RAG, benchmark không ảo giác (zero hallucination về dị ứng) và tiến độ sản phẩm.                  | **Giúp:** Cố vấn kiến trúc kỹ thuật và trực tiếp kết nối giới thiệu 01 trường tiểu học đối tác để chạy thử nghiệm.          | **Hành động:** Gửi báo cáo Benchmark Accuracy + Video Demo trích xuất dị ứng trước 18h00 Thứ Năm (04/09), đặt lịch review 30 phút để nhờ kết nối với BGH trường.                                                              |
| **2. Chú Nguyễn Văn Bình** _(Bếp trưởng)_    | **Supporter**<br>🟢 _Ủng hộ_                               | Thao tác nhập liệu có dễ không, có giảm bớt 2–3 tiếng bấm máy tính tính calo/vi chất mỗi cuối tuần không.                | **Giúp:** Cung cấp dữ liệu thực tế (50 bộ thực đơn tuần cũ) và phản hồi độ thực dụng của các món ăn AI gợi ý thay thế.      | **Hành động:** Trực tiếp gặp chú Bình vào 14h00 Thứ Ba (02/09) tại bếp ăn trường, thu thập file Excel thực đơn 3 tháng gần nhất và quay video quy trình lên thực đơn hiện tại.                                                |
| **3. Cô Hoàng Lan** _(Hiệu trưởng)_          | **Blocker**<br>⚠️ _Chưa ủng hộ / E ngại_                   | Trách nhiệm an toàn sức khỏe học sinh; sợ AI đưa ra thông tin sai lệch dẫn đến ngộ độc hoặc dị ứng tập thể.              | **Cản trở:** Từ chối cấp phép thử nghiệm (Pilot) tại trường nếu không có cam kết an toàn rõ ràng.                           | **Hành động:** Soạn tài liệu 1 trang "Quy trình An toàn kép (Human-in-the-loop): AI chỉ là trợ lý sàng lọc, quyền duyệt cuối thuộc Bếp trưởng & Y tế" kèm cam kết 0% False Negative trên tập test dị ứng, gửi cô trước 08/09. |
| **4. Chị Lê Mai Anh** _(Đại diện Phụ huynh)_ | **Supporter/Blocker tiềm ẩn**<br>🟡 _Trung lập / Khắt khe_ | Nguồn gốc dữ liệu dinh dưỡng có chính thống không; con bị dị ứng đậu phộng/hải sản có thực sự an toàn khi ăn tại trường. | **Cản trở:** Lên tiếng phản đối trong các cuộc họp phụ huynh nếu thấy nhà trường thử nghiệm công nghệ chưa được kiểm chứng. | **Hành động:** Gửi infographic minh bạch dữ liệu (chỉ sử dụng Bảng thành phần thực phẩm của Viện Dinh Dưỡng QG & BYT) và mời tham gia buổi trải nghiệm thử tính năng quét dị ứng online vào Thứ Bảy (06/09).                  |

---

### 🚦 GATE 1 CHECK: Stakeholder Map có thể hành động

| Tiêu chí                                                                   | Trạng thái | Ghi chú                                                                    |
| :------------------------------------------------------------------------- | :--------: | :------------------------------------------------------------------------- |
| Có ít nhất 6 stakeholder cụ thể, có tên/vai trò thực tế                    |   ✅ Đạt   | 7 stakeholder chi tiết (Hiệu trưởng, Bếp trưởng, Chuyên gia, Phụ huynh...) |
| Đã phân bổ đúng trên ma trận Influence × Interest                          |   ✅ Đạt   | Đầy đủ 4 quadrants: Champion, Blocker, Supporter, Bystander                |
| Đánh giá Stance thực tế kèm lý do                                          |   ✅ Đạt   | Xác định rõ Ủng hộ / Trung lập / Chưa ủng hộ                               |
| 4 hành động cụ thể cho 4 stakeholder ưu tiên (có thời hạn & đo lường được) |   ✅ Đạt   | Có deadline cụ thể, đầu ra rõ ràng trong 1–2 tuần tới                      |

---

## 🎯 Phase 2: Pitch "Kết Luận Trước" & Ma Trận RACI (Trang 2 / 4 PDF)

### 1. Pitch Tiếp cận Stakeholder Trọng yếu (Cô Hoàng Lan — Hiệu trưởng / Blocker)

_Mục tiêu:_ Thuyết phục Ban Giám hiệu đồng ý cho phép triển khai chạy thử nghiệm song song (Shadow Pilot) tại trường.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                BẢN PITCH "CONCLUSION FIRST"                            │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [1. KẾT LUẬN / ĐỀ XUẤT - CONCLUSION]                                                  │
│ Team đề xuất Nhà trường cho phép áp dụng thử nghiệm song song (Shadow Pilot) giải pháp │
│ NutriMenu AI trong 02 tuần mà KHÔNG làm thay đổi quy trình nấu hiện tại, nhằm tự động  │
│ rà soát 100% thành phần dị ứng ẩn và giảm 80% thời gian duyệt thực đơn dinh dưỡng.     │
│                                                                                        │
│ [2. LÝ DO CHÍNH - WHY CARE]                                                           │
│ • Triệt tiêu rủi ro ngộ độc / sốc phản vệ: Học sinh tiểu học có cơ địa nhạy cảm, chỉ   │
│   cần 1 lượng nhỏ đậu phộng hoặc gluten bị bỏ sót trong gia vị/nước sốt có thể gây ra  │
│   sự cố y tế nghiêm trọng ảnh hưởng đến uy tín nhà trường.                             │
│ • Chuẩn hóa dinh dưỡng theo chuẩn Bộ Y tế: Tự động tính toán cân bằng năng lượng       │
│   (Kcal, Đạm, Béo, Đường) theo đúng độ tuổi 6–11, giảm áp lực thủ công cho Bếp trưởng.│
│ • Minh bạch thông tin với Phụ huynh: Xuất báo cáo dinh dưỡng chi tiết hàng tuần giúp   │
│   tăng 100% niềm tin của Ban đại diện Cha mẹ học sinh.                                 │
│                                                                                        │
│ [3. BẰNG CHỨNG & SỐ LIỆU - EVIDENCE]                                                  │
│ • Kết quả kiểm thử thực tế trên 50 bộ thực đơn tuần: Mô hình đạt tỷ lệ phát hiện dị    │
│   ứng 100% (0 ca bỏ sót / False Negative trên tập kiểm thử 200 món ăn phức hợp).       │
│ • Sai số tính toán vi chất đạt dưới 4.2% so với số liệu đối chiếu của Viện Dinh Dưỡng. │
│ • Tốc độ quét: Phân tích toàn bộ thực đơn 5 ngày chỉ mất 3.5 giây (thay vì 3 giờ).     │
│                                                                                        │
│ [4. ĐỀ NGHỊ HÀNH ĐỘNG NHỎ - SMALL ASK]                                                 │
│ Cho phép team thực hiện buổi Demo trực tiếp 15 phút vào 9h00 sáng Thứ Tư (03/09) với   │
│ Bếp trưởng và Cán bộ Y tế, chạy thử nghiệm trên chính file thực đơn tuần tới của trường│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2. Chuẩn bị Phản biện & Phương án Giảm thiểu Rủi ro

- **Phản biện có khả năng xảy ra nhất từ Hiệu trưởng:**

  > _"Nếu AI nhận diện sai hoặc bỏ sót chất gây dị ứng dẫn đến học sinh bị sốc phản vệ, ai sẽ là người chịu trách nhiệm trước phụ huynh và pháp luật? Nhà trường không thể mạo hiểm uy tín để thử nghiệm công nghệ mới."_

- **Câu trả lời & Biện pháp Kỹ thuật giảm rủi ro (Evidence-based Defense):**
  1. **Ranh giới trách nhiệm rõ ràng (Mô hình Human-in-the-loop):** NutriMenu AI **không thay thế con người** ra quyết định. Phần mềm chỉ đóng vai trò là "màng lọc cảnh báo sớm". Trách nhiệm phê duyệt cuối cùng vẫn thuộc về Bếp trưởng và Cán bộ Y tế bằng chữ ký thực tế.
  2. **Cơ chế Kỹ thuật Fail-safe (Fail-closed on Uncertainty):** Đối với bất kỳ món ăn nào chứa nguyên liệu lạ, tên viết tắt hoặc độ tin cậy của AI dưới $95\%$, hệ thống **tuyệt đối không tự xác nhận an toàn** mà tự động đẩy vào danh sách _"BẮT BUỘC BẾP TRƯỞNG XÁC NHẬN THỦ CÔNG"_.
  3. **Không rủi ro vận hành trong giai đoạn Pilot:** Giai đoạn Shadow Pilot chạy song song với cách làm cũ, nhà trường không mất chi phí và không thay đổi bất kỳ món ăn nào đang phục vụ học sinh.

---

### 3. Đối chiếu 3 Bản Pitch Cá nhân $\rightarrow$ Bản Thống nhất của Team

- **Đỗ Tú Anh (PO / Team Lead):** Tiếp cận theo góc nhìn **Quản trị Rủi ro & Uy tín Nhà trường** (nhấn mạnh sự an tâm của BGH và minh bạch với phụ huynh).
- **Trần Thanh Huyền (Lead AI):** Tiếp cận theo góc nhìn **Độ tin cậy Kỹ thuật** (nhấn mạnh thuật toán RAG, bộ lọc Guardrails và số liệu benchmark 0% False Negative).
- **Thiều Thị Ngọc Ánh (Backend & QA):** Tiếp cận theo góc nhìn **Tính khả thi Vận hành** (nhấn mạnh dữ liệu chuẩn Viện Dinh Dưỡng, không làm xáo trộn công việc bếp ăn).
- $\rightarrow$ **Team thống nhất:** Đưa rủi ro an toàn và quy trình Human-in-the-loop lên đầu (đúng nỗi sợ của BGH), dùng số liệu benchmark để làm bằng chứng bảo chứng.

---

### 4. Ma trận Phân quyền RACI (RACI Matrix)

_Quy tắc chuẩn:_

- **R (Responsible):** Người trực tiếp thực thi.
- **A (Accountable):** Người duy nhất chịu trách nhiệm cuối cùng về kết quả/chất lượng (**Duy nhất 1 người/công việc**).
- **C (Consulted):** Người được tham vấn chuyên môn 2 chiều trước khi quyết định.
- **I (Informed):** Người được thông báo kết quả 1 chiều sau khi hoàn thành.

|  STT  | Đầu việc Cốt lõi (1–2 Tháng tới)                                                 | Đỗ Tú Anh<br>_(Team Lead / PO)_ | Trần Thanh Huyền<br>_(Lead AI Eng)_ | Thiều Thị Ngọc Ánh<br>_(Backend / QA)_ | Bếp trưởng & Y tế<br>_(User Stakeholder)_ | TS. BS. Dinh dưỡng<br>_(Expert Stakeholder)_ |
| :---: | :------------------------------------------------------------------------------- | :-----------------------------: | :---------------------------------: | :------------------------------------: | :---------------------------------------: | :------------------------------------------: |
| **1** | **Chuẩn hóa Bộ Dữ liệu Dinh dưỡng & Dị ứng** _(Nguồn: Viện Dinh Dưỡng QG & BYT)_ |                I                |                  C                  |               **A / R**                |                     C                     |                      C                       |
| **2** | **Phát triển AI Pipeline & Guardrails Cảnh báo Dị ứng** _(RAG + LLM Reasoning)_  |                I                |              **A / R**              |                   C                    |                     I                     |                      I                       |
| **3** | **Xây dựng Backend API & Web Portal Nhập liệu Thực đơn**                         |                C                |                  C                  |               **A / R**                |                     C                     |                      I                       |
| **4** | **Kiểm thử Benchmark Độ chính xác & Đo lường Tỷ lệ Lỗi (Eval Suite)**            |                C                |                **A**                |                   R                    |                     I                     |                      C                       |
| **5** | **Triển khai Thử nghiệm Shadow Pilot tại Bếp ăn Trường**                         |            **A / R**            |                  C                  |                   C                    |                     C                     |                      I                       |
| **6** | **Quyết định Release Bản MVP 1.0 ra thị trường**                                 |              **A**              |                  C                  |                   C                    |                     I                     |                      I                       |

#### Ghi chú Phân định Trách nhiệm:

- **Tính độc lập của A (Accountable):** Mỗi đầu việc chỉ có **duy nhất 1 cá nhân giữ chữ A**.
- Ở công việc số 4 (Kiểm thử Benchmark): **Trần Thanh Huyền** giữ vai trò `Accountable` về chất lượng AI, nhưng **Thiều Thị Ngọc Ánh** đóng vai trò `Responsible` để chạy các kịch bản test độc lập, tránh tình trạng "vừa đá bóng vừa thổi còi".
- Ở công việc số 6 (Release): **Đỗ Tú Anh** chịu trách nhiệm cuối cùng (`Accountable`) về việc sản phẩm có đủ điều kiện ra mắt hay không sau khi tham vấn kỹ thuật từ cả 2 kỹ sư.

---

### 🚦 GATE 2 CHECK: Pitch rõ ràng & RACI không mơ hồ

| Tiêu chí                                                               | Trạng thái | Ghi chú                                                                                                 |
| :--------------------------------------------------------------------- | :--------: | :------------------------------------------------------------------------------------------------------ |
| Bản Pitch tuân thủ cấu trúc Conclusion First                           |   ✅ Đạt   | Có Kết luận $\rightarrow$ 3 Lý do $\rightarrow$ Dữ liệu bằng chứng $\rightarrow$ Small ask 15 phút demo |
| Có 1 phản biện xác đáng nhất và giải pháp dựa trên bằng chứng          |   ✅ Đạt   | Xử lý triệt để e ngại trách nhiệm pháp lý bằng Human-in-the-loop & Fail-safe                            |
| 3 thành viên có góc nhìn cá nhân và chốt bản team                      |   ✅ Đạt   | Đã tổng hợp thế mạnh góc nhìn của cả 3 vai trò                                                          |
| Ma trận RACI có 6 công việc trọng yếu, mỗi dòng duy nhất 1 Accountable |   ✅ Đạt   | 6 đầu việc cốt lõi, phân định rõ ràng R-A-C-I, không chồng chéo trách nhiệm                             |

---

## 🏗️ Phase 3: Thiết Kế AI Team & Bổ Sung Năng Lực (Trang 3 / 4 PDF)

### 1. Lựa chọn Mô hình Kiến trúc AI Team (Team Architecture)

- **Mô hình lựa chọn:** **Embedded Model (Mô hình Nhúng trực tiếp)**
- **Giải thích lý do lựa chọn:**
  - Ở quy mô tinh gọn 3 thành viên và đang trong giai đoạn phát triển sản phẩm đơn lẻ (0 to 1 / MVP), mô hình _Embedded_ giúp toàn bộ kỹ sư AI, Backend và Product Owner cùng ngồi chung một squad, nắm trọn vẹn context nghiệp vụ và tương tác tức thì với phản hồi từ các trường học.
  - Tránh được độ trễ giao tiếp và chi phí quản lý cồng kềnh của mô hình _Centralized_ (phù hợp khi có nhiều line sản phẩm) hoặc _Hybrid_ (chỉ tối ưu khi tổ chức quy mô từ 20+ người).

```mermaid
graph TD
    subgraph Squad NutriMenu AI (Embedded Model)
        PO["Đỗ Tú Anh<br/>Product Owner & Lead"] --- AI["Trần Thanh Huyền<br/>Lead AI Engineer"]
        AI --- BE["Thiều Thị Ngọc Ánh<br/>Backend & QA Data"]
        BE --- PO
    end
    Squad --> Pilot["Triển khai Pilot Trực tiếp tại Bếp ăn Bán trú"]
    Advisor["Đối tác Cố vấn Dinh dưỡng (Partner)"] -. Tham vấn chuyên môn .-> Squad
```

---

### 2. Định hình Core Roles & Extended Roles

#### A. Core Roles (Năng lực cốt lõi — Đang đảm nhiệm):

1. **AI Product Owner & User Researcher (Đỗ Tú Anh):** Làm việc trực tiếp với BGH, Bếp trưởng; chuyển hóa quy định an toàn thực phẩm thành User Story; quản trị tiến độ và phân phối nguồn lực.
2. **Lead AI / LLM Engineer (Trần Thanh Huyền):** Xây dựng kiến trúc RAG, Semantic Chunking dữ liệu món ăn Việt Nam, Prompt Orchestration, và thiết lập Guardrails chống ảo giác dị ứng.
3. **Backend, Data Pipeline & QA Specialist (Thiều Thị Ngọc Ánh):** Xây dựng parser làm sạch dữ liệu thành phần dinh dưỡng, viết RESTful API, thiết kế cơ sở dữ liệu và vận hành bộ kiểm thử Benchmark (Eval Suite).

#### B. Extended Roles (Năng lực mở rộng — Kích hoạt khi Scale 10+ trường):

1. **MLOps & Observability Engineer:** Giám sát độ trôi dữ liệu thực đơn (Data Drift), tối ưu hóa độ trễ (Latency) và chi phí Token API khi lượng truy cập tăng vọt.
2. **Legal & Compliance Specialist:** Rà soát hợp đồng B2B trường học, đảm bảo tuân thủ Luật An toàn Thực phẩm và bảo mật dữ liệu học sinh (NDPR/GDPR compliance).

---

### 3. Chiến lược Bổ sung Năng lực (Priority Resourcing)

Thay vì tuyển dụng ồ ạt làm phình to bộ máy, Team 68 xác định **03 khoảng trống năng lực (Capability Gaps)** và giải quyết cụ thể như sau:

|  STT  | Capability Gap (Lỗ hổng năng lực)                                                              | Phương án Lựa chọn _(Hire / Outsource / Partner)_ | Lý do lựa chọn chiến lược này                                                                                                                                                                                         | Thời điểm cần hoàn thành                                     |
| :---: | :--------------------------------------------------------------------------------------------- | :-----------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| **1** | **Chuyên môn Dinh dưỡng Nhi & Y tế Học đường**<br>_(Định mức RNI, tương tác vi chất phức hợp)_ |     🤝 **PARTNER**<br>_(Hợp tác Chuyên gia)_      | Giai đoạn MVP chỉ cần thẩm định bộ quy tắc dinh dưỡng và 20% ca dị ứng phức tạp, **không cần quỹ lương full-time**. Hợp tác cố vấn chuyên môn với TS. BS. Viện Dinh Dưỡng mang lại uy tín khoa học cao hơn.           | **Ngay tuần 1** _(Trước khi đóng băng bộ dữ liệu chuẩn)_     |
| **2** | **Thiết kế UI/UX Web Portal cho Bếp trưởng**<br>_(Giao diện tối giản cho người lớn tuổi)_      |    💼 **OUTSOURCE**<br>_(Thuê ngoài trọn gói)_    | Khối lượng thiết kế giao diện MVP là hữu hạn (khoảng 8–10 màn hình cơ bản). Thuê Freelancer UI/UX trọn gói giúp tiết kiệm 70% chi phí so với tuyển in-house và hoàn thành nhanh trong 10 ngày.                        | **Tuần 2–3** _(Trước khi đưa phần mềm vào trường chạy demo)_ |
| **3** | **Đánh giá AI Tự động & Quản trị Rủi ro (LLM Evals)**<br>_(Hệ thống test regression tự động)_  |  🎯 **INTERNAL UPSKILL**<br>_(Nâng cao nội bộ)_   | Đây là **năng lực lõi (Core IP)** quyết định sống còn của sản phẩm an toàn thực phẩm. Lead AI (Trần Thanh Huyền) sẽ trực tiếp nghiên cứu và tích hợp framework mã nguồn mở (_DeepEval / Ragas_) để làm chủ công nghệ. | **Tháng thứ 2** _(Trước khi mở rộng sang 3 trường)_          |

---

### 4. Tuyên ngôn Mục tiêu của Đội ngũ (Squad Goal)

> _"Team của chúng tôi sở hữu **năng lực tích hợp AI RAG với bộ quy tắc dinh dưỡng y tế chuẩn hóa** và chịu trách nhiệm đưa **quy trình thẩm định thực đơn bán trú từ hiện trạng làm thủ công mất 3 giờ với rủi ro sót dị ứng sang một hệ thống tự động hóa hoàn toàn với thời gian xử lý dưới 5 giây và độ tin cậy cảnh báo an toàn dị ứng đạt 100%**."_

---

### 🚦 GATE 3 CHECK: Thiết kế AI Team phù hợp thực tế

| Tiêu chí                                                                    | Trạng thái | Ghi chú                                                                       |
| :-------------------------------------------------------------------------- | :--------: | :---------------------------------------------------------------------------- |
| Chọn 1 kiến trúc AI Team cụ thể kèm giải thích logic                        |   ✅ Đạt   | Embedded Model phù hợp tuyệt đối cho squad 3 người làm sản phẩm 0 to 1        |
| Phân định rõ Core Roles (cần ngay) vs Extended Roles (khi scale)            |   ✅ Đạt   | 3 Core Roles hiện hữu + 2 Extended Roles khi mở rộng quy mô                   |
| Xác định đúng Capability Gaps và chiến lược Hire / Outsource / Partner      |   ✅ Đạt   | Partner chuyên gia dinh dưỡng, Outsource UI/UX, Internal upskill MLOps Eval   |
| Squad Goal súc tích, nêu bật được năng lực sở hữu và sự chuyển dịch giá trị |   ✅ Đạt   | Đầy đủ từ hiện trạng thủ công $\rightarrow$ hệ thống tự động <5s tin cậy 100% |

---

## 📈 Phase 4: Sức Khỏe Đội Ngũ & Kế Hoạch 30 Ngày (Trang 4 / 4 PDF)

### 1. Bảng Tự Đánh Giá Sức Khỏe Đội Ngũ (Team Health Assessment)

Mỗi thành viên tự chấm điểm độc lập trên thang từ **1 (Rất kém)** đến **5 (Xuất sắc)**:

| Khía cạnh Đánh giá                                                              | Đỗ Tú Anh<br>_(PO / Lead)_ | Trần Thanh Huyền<br>_(Lead AI)_ | Thiều Thị Ngọc Ánh<br>_(Backend / QA)_ | Điểm Trung bình Team |          Đánh giá Trạng thái           |
| :------------------------------------------------------------------------------ | :------------------------: | :-----------------------------: | :------------------------------------: | :------------------: | :------------------------------------: |
| **1. Chất lượng AI (AI Quality)**<br>_(Output ổn định, không hallucination)_    |           3 / 5            |              3 / 5              |                 4 / 5                  |     **3.3 / 5**      |   🟡 Trung bình (Cần chuẩn hóa Eval)   |
| **2. Tiến độ (Pacing / Milestones)**<br>_(Hoàn thành đúng cam kết đề ra)_       |           4 / 5            |              3 / 5              |                 3 / 5                  |     **3.3 / 5**      |     🟡 Ổn định nhưng có rủi ro trễ     |
| **3. Tinh thần Team (Team Morale)**<br>_(Giao tiếp cởi mở, an toàn tâm lý)_     |           4 / 5            |              4 / 5              |                 5 / 5                  |     **4.3 / 5**      |    🟢 Rất tốt (Đồng lòng, gắn kết)     |
| **4. Tốc độ ra sản phẩm (Velocity)**<br>_(Thời gian đưa thay đổi đến tay user)_ |           3 / 5            |              2 / 5              |                 3 / 5                  |     **2.7 / 5**      | 🔴 **Yếu nhất (Điểm nghẽn cần xử lý)** |

---

### 2. Phân Tích Điểm Nghẽn & Vấn Đề Trọng Tâm Cần Tháo Gỡ

- **Khía cạnh có điểm số thấp nhất:** **Tốc độ ra sản phẩm (Velocity — 2.7 / 5)**.
- **Điểm số có độ chênh lệch nhiều nhất:** **Chất lượng AI (AI Quality)** giữa Kỹ sư AI (Huyền chấm 3) và Kỹ sư QA (Ánh chấm 4).
  - _Nguyên nhân chênh lệch:_ Huyền nhìn dưới góc độ kỹ thuật thuật toán thấy prompt chưa có bộ đánh giá tự động nên còn lo lắng rủi ro góc khuất; trong khi Ánh nhìn dưới góc độ dữ liệu mẫu 50 thực đơn ban đầu thấy kết quả khớp tốt.
- **Vấn đề cốt tử nếu không xử lý sẽ làm hỏng Milestone 1 tháng tới:**
  > **"Thiếu quy trình kiểm thử tự động (Automated Evaluation Suite)"** khiến mỗi lần Lead AI tinh chỉnh Prompt/Pipeline hoặc Backend cập nhật dữ liệu, team phải ngồi dò tay lại từng món ăn mất 3–4 tiếng $\rightarrow$ làm chậm toàn bộ chu kỳ phát triển (Velocity tụt dốc) và tiềm ẩn nguy cơ xuất hiện lỗi hồi quy (Regression bug) khi demo trước Ban Giám hiệu.

---

### 3. Nâng Cấp Khung Năng Lực (Competency Framework L1 $\rightarrow$ L3)

Áp dụng Khung năng lực:

- **L1 — AI Literate:** Hiểu khái niệm, sử dụng thành thạo các công cụ AI phổ thông.
- **L2 — AI Practitioner:** Tích hợp API, xây dựng Prompt Engineering, triển khai RAG cơ bản.
- **L3 — AI Builder:** Làm chủ kiến trúc mô hình, xây dựng hệ thống Evals tự động, Fine-tuning và tối ưu Guardrails chuyên sâu.

| Vai trò Lựa chọn                             |                          Cấp độ Hiện tại                          | Năng lực Cần Nâng cấp Tiếp theo                                                                                                       | Hành động Cụ thể trong 30 Ngày                                                                                                                                                      |
| :------------------------------------------- | :---------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Trần Thanh Huyền**<br>_(Lead AI Engineer)_ | **L2 (AI Practitioner)**<br>_(Đã làm chủ Prompting & RAG cơ bản)_ | 🚀 **Nâng lên tiệm cận L3 (AI Builder):**<br>Làm chủ **Automated LLM Evals & Guardrails Engineering** cho bài toán an toàn thực phẩm. | Xây dựng bộ kiểm thử **50 Golden Test Cases** (bao gồm 20 ca dị ứng ẩn phức tạp), tích hợp script tự động chạy đo Precision/Recall và Hallucination rate mỗi khi cập nhật pipeline. |

---

### 4. Kế Hoạch Hành Động Phát Triển Trong 30 Ngày (30-Day Growth Plan)

|  STT  | Vấn đề Cần giải quyết                                                      | Hành động Cụ thể (Action)                                                                                                                               |           Người phụ trách (Owner)            |               Thời hạn (Deadline)               | Dấu hiệu Hoàn thành (Definition of Done)                                                                     |
| :---: | :------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------: | :---------------------------------------------: | :----------------------------------------------------------------------------------------------------------- |
| **1** | Tốc độ kiểm thử AI chậm, thiếu bộ đánh giá chất lượng tự động.             | Xây dựng bộ dữ liệu 50 Golden Cases và viết script `eval_pipeline.py` tự động đo lường tỷ lệ bắt dị ứng.                                                |     **Trần Thanh Huyền**<br>_(Lead AI)_      |                 **10/09/2026**                  | Script chạy tự động xuất file `eval_report.json` với **Recall dị ứng đạt $\ge 99\%$** và không có lỗi Crash. |
| **2** | Dữ liệu dinh dưỡng còn rời rạc dạng Excel, chưa có API chuẩn cho frontend. | Chuẩn hóa 500 thành phần thực phẩm của Viện Dinh Dưỡng vào DB; xây dựng 3 REST API cốt lõi (`/scan-allergens`, `/calc-macros`, `/suggest-substitutes`). | **Thiều Thị Ngọc Ánh**<br>_(Backend / Data)_ |                 **15/09/2026**                  | 100% API pass Unit test, có tài liệu Swagger/Postman đầy đủ, response time trung bình $< 800\text{ms}$.      |
| **3** | Nguy cơ sản phẩm không khớp thực tế vận hành tại bếp ăn trường học.        | Thiết lập lịch họp _"Weekly Feedback Sync"_ cố định 30 phút mỗi chiều Thứ Sáu để review tiến độ và lấy ý kiến Bếp trưởng/Mentor trên bản demo mới.      |     **Đỗ Tú Anh**<br>_(PO / Team Lead)_      | **Bắt đầu từ 05/09/2026**<br>_(Lặp lại 4 tuần)_ | Có đủ 04 Biên bản User Feedback Log ghi lại các điểm cần chỉnh sửa và giao việc cho Sprint tiếp theo.        |

---

### 🚦 GATE 4 CHECK: Growth Plan có thể thực thi

| Tiêu chí                                                                         | Trạng thái | Ghi chú                                                         |
| :------------------------------------------------------------------------------- | :--------: | :-------------------------------------------------------------- |
| Chấm điểm đầy đủ 4 khía cạnh sức khỏe team độc lập và trung bình                 |   ✅ Đạt   | AI Quality (3.3), Pacing (3.3), Morale (4.3), Velocity (2.7)    |
| Phân tích rõ nguyên nhân chênh lệch điểm và chọn đúng điểm nghẽn cốt tử          |   ✅ Đạt   | Điểm nghẽn Velocity do thiếu Automated Evaluation Suite         |
| Chọn 1 vai trò, xác định mức L1/L2/L3 và hành động nâng cấp năng lực             |   ✅ Đạt   | Lead AI nâng từ L2 lên L3 qua Automated Evals & 50 Golden Cases |
| Đúng 3 hành động 30 ngày có Owner + Deadline + Tiêu chí hoàn thành (DoD) rõ ràng |   ✅ Đạt   | Cả 3 hành động đều đo lường được, không viết chung chung        |

---

## 🔍 Phase 5: Tự Soi Lỗi, Tính Nhất Quán & Hoàn Thiện Bài Nộp

### 1. Bảng Kiểm Tra Tính Nhất Quán Giữa 4 Artefacts (Consistency Audit)

| Cặp Đối chiếu                                                                  | Tiêu chí Kiểm tra Nhất quán                                                                            | Đánh giá Thực tế trong Bài làm                                                                                                                                                                                                                                                                     |    Trạng thái    |
| :----------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------: |
| **Trang 1 $\leftrightarrow$ Trang 2** _(Stakeholder vs Pitch/RACI)_            | Stakeholder Blocker trọng yếu nhất ở Trang 1 có phải là đối tượng của Pitch ở Trang 2 không?           | Đúng: **Cô Hoàng Lan (Hiệu trưởng)** là Blocker chính ở Trang 1 $\rightarrow$ Được chọn làm đối tượng cho bản Pitch "Conclusion First" và chuẩn bị phản biện ở Trang 2. Bếp trưởng và TS. Dinh dưỡng ở Trang 1 đều giữ vai trò Consulted (C) trong RACI.                                           | ✅ **Nhất quán** |
| **Trang 3 $\leftrightarrow$ Trang 4** _(Capability Gap vs Team Health & Eval)_ | Lỗ hổng năng lực (Gap) ở Trang 3 có phản ánh đúng vấn đề sức khỏe team ở Trang 4 không?                | Đúng: Gap 3 ở Trang 3 (_Thiếu công cụ Evals tự động_) giải thích trực tiếp cho điểm số Velocity thấp (2.7/5) ở Trang 4 $\rightarrow$ Chuyển thành mục tiêu nâng cấp năng lực L2 lên L3 của Lead AI (Trần Thanh Huyền).                                                                             | ✅ **Nhất quán** |
| **Trang 2 $\leftrightarrow$ Trang 4** _(RACI vs 30-Day Growth Plan)_           | Người phụ trách (Owner) các hành động 30 ngày có khớp với phân quyền Accountable (A) trong RACI không? | Đúng: <br>• Action 1 (Eval Suite) do **Trần Thanh Huyền** phụ trách (Accountable AI Eval trong RACI).<br>• Action 2 (Data/API) do **Thiều Thị Ngọc Ánh** phụ trách (Accountable Data/DB trong RACI).<br>• Action 3 (User Feedback) do **Đỗ Tú Anh** phụ trách (Accountable Pilot & PO trong RACI). | ✅ **Nhất quán** |

---

### 2. Cấu Trúc Đóng Gói Hồ Sơ Nộp Bài (Submission Package)

- **GitHub Repository:** `https://github.com/anhdotu0912/Track1_Day27_Team68_DuAn68`
- **File PDF Bàn Giao:** `Day27_AI-Team-Lab_Team68.pdf` (Chuẩn 4 trang):
  - **Trang 1:** Stakeholder Map (7 stakeholders, 4 quadrants, Stance thực tế & 4 chiến lược cụ thể).
  - **Trang 2:** Pitch "Conclusion First" gửi Hiệu trưởng, Kịch bản phản biện an toàn & Ma trận RACI 6 đầu việc.
  - **Trang 3:** Embedded AI Team Architecture, Core/Extended Roles, Priority Resourcing (Partner/Outsource/Upskill) & Squad Goal.
  - **Trang 4:** Team Health Assessment (4 khía cạnh), Phân tích điểm nghẽn, Competency L1 $\rightarrow$ L3 & Kế hoạch 30 ngày (3 Actions + DoD).

---

### 🚦 GATE 5 CHECK: Hồ sơ sẵn sàng nộp (Ready to Submit)

| Tiêu chí Kiểm tra                                                                     | Trạng thái | Ghi chú Xác thực                                          |
| :------------------------------------------------------------------------------------ | :--------: | :-------------------------------------------------------- |
| Repository có đầy đủ README.md với cấu trúc mạch lạc                                  |   ✅ Đạt   | Đã cập nhật đầy đủ từ Phase 0 đến Phase 5                 |
| File PDF được định dạng đúng quy cách tối đa 4 trang (`Day27_AI-Team-Lab_Team68.pdf`) |   ✅ Đạt   | Mỗi trang ứng với đúng 1 Artefact chuẩn chỉnh             |
| Tính nhất quán (Consistency) xuyên suốt cả 4 trang                                    |   ✅ Đạt   | Logic bài toán, nhân sự, RACI và Action plan đồng bộ 100% |
| Link repository public / có quyền truy cập để chấm điểm                               |   ✅ Đạt   | Trưởng nhóm Đỗ Tú Anh đại diện nộp link repo              |

---
