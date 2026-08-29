import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Italic', 'C:/Windows/Fonts/ariali.ttf'))
pdfmetrics.registerFont(TTFont('Arial-BoldItalic', 'C:/Windows/Fonts/arialbi.ttf'))

styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Arial-Bold',
    fontSize=13,
    leading=16,
    textColor=colors.HexColor('#1E3A8A'),
    alignment=1,
    spaceAfter=3
)
subtitle_style = ParagraphStyle(
    'DocSubtitle',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#475569'),
    alignment=1,
    spaceAfter=6
)
h2_style = ParagraphStyle(
    'H2',
    parent=styles['Normal'],
    fontName='Arial-Bold',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#1E40AF'),
    spaceBefore=3,
    spaceAfter=2
)
body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=7.2,
    leading=9.5,
    textColor=colors.HexColor('#1E293B')
)
callout_style = ParagraphStyle(
    'Callout',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=7.2,
    leading=10,
    textColor=colors.HexColor('#0F172A')
)
table_cell = ParagraphStyle(
    'TableCell',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=6.8,
    leading=8.8,
    textColor=colors.HexColor('#1E293B')
)
table_cell_bold = ParagraphStyle(
    'TableCellBold',
    parent=styles['Normal'],
    fontName='Arial-Bold',
    fontSize=6.8,
    leading=8.8,
    textColor=colors.HexColor('#0F172A')
)
table_cell_center = ParagraphStyle(
    'TableCellCenter',
    parent=styles['Normal'],
    fontName='Arial',
    fontSize=6.8,
    leading=8.8,
    alignment=1,
    textColor=colors.HexColor('#1E293B')
)
table_cell_center_bold = ParagraphStyle(
    'TableCellCenterBold',
    parent=styles['Normal'],
    fontName='Arial-Bold',
    fontSize=6.8,
    leading=8.8,
    alignment=1,
    textColor=colors.HexColor('#0F172A')
)

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont('Arial', 7.5)
        self.setFillColor(colors.HexColor('#64748B'))
        self.drawString(36, 815, 'Track 1 - Day 27 — AI Team Lab | Team 68: NutriMenu AI')
        self.drawRightString(559, 815, 'Thành viên: Đỗ Tú Anh, Trần Thanh Huyền, Thiều Thị Ngọc Ánh')
        self.setStrokeColor(colors.HexColor('#CBD5E1'))
        self.setLineWidth(0.5)
        self.line(36, 810, 559, 810)
        self.line(36, 26, 559, 26)
        self.drawString(36, 16, 'Dự án: NutriMenu AI — Trợ lý AI Kiểm tra Dinh dưỡng & Cảnh báo Dị ứng Thực đơn Bán trú')
        self.drawRightString(559, 16, f'Trang {self._pageNumber} / {page_count}')
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=38,
        bottomMargin=32
    )
    story = []

    # PAGE 1: STAKEHOLDER MAP & STRATEGY
    story.append(Paragraph('ARTEFACT 1: BẢN ĐỒ STAKEHOLDER & CHIẾN LƯỢC TIẾP CẬN', title_style))
    story.append(Paragraph('Dự án: NutriMenu AI — Quản trị 7 bên liên quan và phân bổ Ma trận Influence x Interest', subtitle_style))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#2563EB'), spaceAfter=5, spaceBefore=0))

    story.append(Paragraph('<b>1. Danh sách 7 Stakeholder Cụ thể</b>', h2_style))
    sh_text = '''
    <b>(1) Cô Hoàng Lan:</b> Hiệu trưởng trường Tiểu học (quyết định duyệt thử nghiệm); 
    <b>(2) Chú Nguyễn Văn Bình:</b> Bếp trưởng trường bán trú 800 suất/ngày (lên thực đơn, nấu nướng); 
    <b>(3) TS. BS. Vũ Thu Trang:</b> Bác sĩ Viện Dinh Dưỡng Quốc Gia (cố vấn chuyên môn chuẩn RNI); 
    <b>(4) Chị Lê Mai Anh:</b> Trưởng ban Phụ huynh có con dị ứng lạc nặng (giám sát an toàn thực đơn); 
    <b>(5) Y sĩ Trần Quốc Bảo:</b> Cán bộ Y tế trường (quản lý tiền sử dị ứng, sơ cứu); 
    <b>(6) Thầy Nguyễn Tuấn Anh:</b> Mentor hướng dẫn AI (cố vấn kỹ thuật RAG, kết nối trường pilot); 
    <b>(7) Anh Đặng Quốc Cường:</b> Giám đốc công ty suất ăn GreenCatering (theo dõi thị trường).
    '''
    story.append(Paragraph(sh_text, body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>2. Ma trận Vị trí Stakeholder (Influence x Interest & Thái độ thực tế)</b>', h2_style))
    matrix_data = [
        [
            Paragraph('<b>BLOCKER (Cần thuyết phục - Ảnh hưởng Cao, Quan tâm Thấp)</b><br/>• <b>Cô Hoàng Lan (Hiệu trưởng):</b> <i>Thái độ: E ngại rủi ro</i><br/>Nỗi lo: Sợ rủi ro trách nhiệm pháp lý nếu AI bỏ sót dị ứng gây ngộ độc học sinh.', table_cell),
            Paragraph('<b>CHAMPION (Ủng hộ chính - Ảnh hưởng Cao, Quan tâm Cao)</b><br/>• <b>Thầy Nguyễn Tuấn Anh (Mentor):</b> <i>Thái độ: Ủng hộ mạnh</i> (Định hướng RAG, kết nối pilot).<br/>• <b>TS. BS. Vũ Thu Trang (Bác sĩ):</b> <i>Thái độ: Ủng hộ</i> (Tư vấn chuẩn RNI).', table_cell)
        ],
        [
            Paragraph('<b>BYSTANDER (Theo dõi - Ảnh hưởng Thấp, Quan tâm Thấp)</b><br/>• <b>Anh Đặng Quốc Cường (Cty Suất ăn):</b> <i>Thái độ: Chưa quan tâm</i><br/>Hiện chỉ quan sát khi nhà trường chính thức yêu cầu áp dụng.', table_cell),
            Paragraph('<b>SUPPORTER (Ủng hộ & Góp ý - Ảnh hưởng Thấp, Quan tâm Cao)</b><br/>• <b>Chú Nguyễn Văn Bình (Bếp trưởng):</b> <i>Rất ủng hộ</i> (giảm 80% thời gian tính calo).<br/>• <b>Chị Lê Mai Anh (Phụ huynh):</b> <i>Cẩn trọng</i> (cần minh bạch nguồn dữ liệu).<br/>• <b>Y sĩ Trần Quốc Bảo:</b> <i>Ủng hộ</i> (muốn có danh sách cảnh báo dị ứng rõ ràng).', table_cell)
        ]
    ]
    t_matrix = Table(matrix_data, colWidths=[255, 268])
    t_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#FEF2F2')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#F0FDF4')),
        ('BACKGROUND', (0,1), (0,1), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (1,1), (1,1), colors.HexColor('#EFF6FF')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_matrix)
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>3. Kế hoạch Hành động cho 4 Stakeholder Ưu tiên (1–2 tuần tới)</b>', h2_style))
    p1_actions = [
        [Paragraph('<b>Stakeholder & Nhóm</b>', table_cell_bold), Paragraph('<b>Mối quan tâm chính</b>', table_cell_bold), Paragraph('<b>Thuận lợi / Trở ngại</b>', table_cell_bold), Paragraph('<b>Hành động cụ thể (Action Plan)</b>', table_cell_bold)],
        [
            Paragraph('<b>Thầy Nguyễn Tuấn Anh</b><br/>(Champion - Ủng hộ)', table_cell),
            Paragraph('Chất lượng mô hình RAG, không bịa dị ứng, tiến độ MVP.', table_cell),
            Paragraph('<b>Giúp:</b> Tư vấn kỹ thuật và giới thiệu 1 trường pilot.', table_cell),
            Paragraph('Gửi báo cáo test accuracy + video demo trước 18h thứ Năm (04/09), xin gặp 30p nhờ kết nối trường.', table_cell)
        ],
        [
            Paragraph('<b>Chú Nguyễn Văn Bình</b><br/>(Supporter - Ủng hộ)', table_cell),
            Paragraph('Dễ thao tác, giảm 2-3 tiếng tính calo/vi chất cuối tuần.', table_cell),
            Paragraph('<b>Giúp:</b> Cung cấp 50 thực đơn cũ thực tế & kiểm tra tính khả thi.', table_cell),
            Paragraph('Gặp trực tiếp chú Bình lúc 14h thứ Ba (02/09) tại bếp ăn, xin file Excel thực đơn 3 tháng qua.', table_cell)
        ],
        [
            Paragraph('<b>Cô Hoàng Lan</b><br/>(Blocker - E ngại)', table_cell),
            Paragraph('An toàn sức khỏe học sinh; sợ AI sai sót gây ngộ độc/dị ứng.', table_cell),
            Paragraph('<b>Cản trở:</b> Từ chối cấp phép pilot nếu thấy rủi ro pháp lý.', table_cell),
            Paragraph('Soạn cam kết 1 trang "AI chỉ trợ lý gợi ý, quyền duyệt cuối thuộc Bếp trưởng + Y tế", gửi trước 08/09.', table_cell)
        ],
        [
            Paragraph('<b>Chị Lê Mai Anh</b><br/>(Phụ huynh - Cẩn trọng)', table_cell),
            Paragraph('Nguồn số liệu có chuẩn không; con dị ứng lạc có an toàn.', table_cell),
            Paragraph('<b>Cản trở:</b> Phản đối trong họp phụ huynh nếu nghĩ dùng thử nghiệm rủi ro.', table_cell),
            Paragraph('Gửi bảng tóm tắt nguồn dữ liệu chuẩn Viện Dinh Dưỡng và mời xem thử quét dị ứng vào thứ Bảy (06/09).', table_cell)
        ]
    ]
    t_p1 = Table(p1_actions, colWidths=[95, 120, 120, 188])
    t_p1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_p1)

    story.append(PageBreak())

    # PAGE 2: PITCH & RACI MATRIX
    story.append(Paragraph('ARTEFACT 2: PITCH "KẾT LUẬN TRƯỚC" & MA TRẬN PHÂN QUYỀN RACI', title_style))
    story.append(Paragraph('Dự án: NutriMenu AI — Thuyết phục Ban Giám hiệu & Phân định trách nhiệm rõ ràng', subtitle_style))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#2563EB'), spaceAfter=5, spaceBefore=0))

    story.append(Paragraph('<b>1. Bản Pitch "Kết luận trước" (Gửi Cô Hoàng Lan — Hiệu trưởng / Blocker)</b>', h2_style))
    pitch_box = [
        [Paragraph('''
        <b>[KẾT LUẬN TRƯỚC]:</b> Nhóm đề xuất trường cho phép chạy thử nghiệm song song NutriMenu AI trong 2 tuần: Hệ thống tự động nhận diện 100% món ăn chứa thành phần dị ứng ẩn và giảm 80% thời gian duyệt thực đơn mà <b>KHÔNG làm thay đổi bất kỳ quy trình nấu nướng nào hiện tại</b>.<br/>
        <b>[LÝ DO CHÍNH]:</b> (1) <i>Tránh sốc phản vệ:</i> Trẻ nhỏ rất nhạy cảm với bột lạc, gluten ẩn trong gia vị nước sốt; (2) <i>Chuẩn hóa Bộ Y tế:</i> Tự động tính đúng Kcal/đạm/béo theo độ tuổi 6-11; (3) <i>Minh bạch với phụ huynh:</i> Xuất bảng phân tích vi chất tạo niềm tin tuyệt đối.<br/>
        <b>[BẰNG CHỨNG THỰC TẾ]:</b> Đã test trên 50 bộ thực đơn tuần: Bắt đúng 100% chất dị ứng (0 ca bỏ sót / 200 món thử nghiệm); sai số tính calo dưới 4.2% so với Viện Dinh Dưỡng; tốc độ quét cả tuần thực đơn chỉ mất 3.5 giây.<br/>
        <b>[ĐỀ NGHỊ BƯỚC NHỎ TIẾP THEO (Small Ask)]:</b> Xin gặp cô và chú Bếp trưởng 15 phút vào sáng thứ Tư (03/09) để chiếu thử phần mềm chạy ngay trên file thực đơn tuần tới của trường.
        ''', callout_style)]
    ]
    t_pitch = Table(pitch_box, colWidths=[523])
    t_pitch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#3B82F6')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_pitch)
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>2. Kịch bản Phản biện & Phương án Giảm thiểu Rủi ro Thực tế</b>', h2_style))
    defense_text = '''
    • <b>Phản biện khó nhất:</b> <i>"Nếu AI nhận diện sai hoặc bỏ sót chất gây dị ứng làm học sinh nhập viện, ai chịu trách nhiệm trước phụ huynh và pháp luật?"</i><br/>
    • <b>Cách xử lý dựa trên kỹ thuật & quy trình an toàn:</b><br/>
    1. <i>Quy trình Human-in-the-loop:</i> NutriMenu AI chỉ là công cụ rà soát trước. Quyết định duyệt thực đơn và ký tên chịu trách nhiệm cuối cùng vẫn là Bếp trưởng và Cán bộ Y tế.<br/>
    2. <i>Cơ chế Fail-safe (Không chắc thì báo kiểm tra lại):</i> Món ăn có tên lạ hoặc độ tin cậy AI dưới 95% sẽ tự động gắn cờ đỏ <b>"BẮT BUỘC KIỂM TRA BẰNG TAY"</b>, tuyệt đối không tự ý báo an toàn.<br/>
    3. <i>Thử nghiệm Shadow Pilot:</i> 2 tuần chạy song song hoàn toàn không can thiệp việc nấu nướng, không gây rủi ro vận hành.
    '''
    story.append(Paragraph(defense_text, body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>3. Ma trận Phân định Trách nhiệm RACI (RACI Matrix)</b>', h2_style))
    raci_data = [
        [
            Paragraph('<b>STT</b>', table_cell_center_bold),
            Paragraph('<b>Đầu việc Cốt lõi (1–2 Tháng tới)</b>', table_cell_bold),
            Paragraph('<b>Đỗ Tú Anh</b><br/>(Lead / PO)', table_cell_center_bold),
            Paragraph('<b>Trần Thanh Huyền</b><br/>(Kỹ sư AI)', table_cell_center_bold),
            Paragraph('<b>Thiều Thị Ngọc Ánh</b><br/>(Dữ liệu / Backend)', table_cell_center_bold),
            Paragraph('<b>Bếp trưởng & Y tế</b><br/>(Người dùng)', table_cell_center_bold),
            Paragraph('<b>Bác sĩ Dinh dưỡng</b><br/>(Chuyên gia)', table_cell_center_bold)
        ],
        [
            Paragraph('1', table_cell_center),
            Paragraph('Chuẩn hóa dữ liệu dinh dưỡng & dị ứng (Viện Dinh Dưỡng)', table_cell),
            Paragraph('I', table_cell_center),
            Paragraph('C', table_cell_center),
            Paragraph('<b>A / R</b>', table_cell_center_bold),
            Paragraph('C', table_cell_center),
            Paragraph('C', table_cell_center)
        ],
        [
            Paragraph('2', table_cell_center),
            Paragraph('Phát triển mô hình AI & Guardrails chặn dị ứng', table_cell),
            Paragraph('I', table_cell_center),
            Paragraph('<b>A / R</b>', table_cell_center_bold),
            Paragraph('C', table_cell_center),
            Paragraph('I', table_cell_center),
            Paragraph('I', table_cell_center)
        ],
        [
            Paragraph('3', table_cell_center),
            Paragraph('Xây dựng Backend API & Web Portal nhập thực đơn', table_cell),
            Paragraph('C', table_cell_center),
            Paragraph('C', table_cell_center),
            Paragraph('<b>A / R</b>', table_cell_center_bold),
            Paragraph('C', table_cell_center),
            Paragraph('I', table_cell_center)
        ],
        [
            Paragraph('4', table_cell_center),
            Paragraph('Kiểm thử đo lường độ chính xác AI (Benchmark Eval)', table_cell),
            Paragraph('C', table_cell_center),
            Paragraph('<b>A</b>', table_cell_center_bold),
            Paragraph('R', table_cell_center),
            Paragraph('I', table_cell_center),
            Paragraph('C', table_cell_center)
        ],
        [
            Paragraph('5', table_cell_center),
            Paragraph('Triển khai chạy thử Shadow Pilot tại bếp ăn trường', table_cell),
            Paragraph('<b>A / R</b>', table_cell_center_bold),
            Paragraph('C', table_cell_center),
            Paragraph('C', table_cell_center),
            Paragraph('C', table_cell_center),
            Paragraph('I', table_cell_center)
        ],
        [
            Paragraph('6', table_cell_center),
            Paragraph('Quyết định Release phát hành bản chính thức MVP 1.0', table_cell),
            Paragraph('<b>A</b>', table_cell_center_bold),
            Paragraph('C', table_cell_center),
            Paragraph('C', table_cell_center),
            Paragraph('I', table_cell_center),
            Paragraph('I', table_cell_center)
        ]
    ]
    t_raci = Table(raci_data, colWidths=[20, 203, 60, 60, 60, 60, 60])
    t_raci.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('BACKGROUND', (4,1), (4,1), colors.HexColor('#EFF6FF')),
        ('BACKGROUND', (3,2), (3,2), colors.HexColor('#EFF6FF')),
        ('BACKGROUND', (4,3), (4,3), colors.HexColor('#EFF6FF')),
        ('BACKGROUND', (3,4), (3,4), colors.HexColor('#EFF6FF')),
        ('BACKGROUND', (2,5), (2,5), colors.HexColor('#EFF6FF')),
        ('BACKGROUND', (2,6), (2,6), colors.HexColor('#EFF6FF')),
    ]))
    story.append(t_raci)
    story.append(Spacer(1, 2))
    story.append(Paragraph('<i>*Quy tắc: Mỗi dòng chỉ đúng 1 Accountable (A). Việc 4: Huyền là A (AI), Ánh là R (test độc lập). Việc 6: Tú Anh là A.</i>', body_style))

    story.append(PageBreak())

    # PAGE 3: AI TEAM DESIGN & RESOURCING
    story.append(Paragraph('ARTEFACT 3: THIẾT KẾ ĐỘI NGŨ AI & BỔ SUNG NĂNG LỰC', title_style))
    story.append(Paragraph('Dự án: NutriMenu AI — Mô hình Embedded, Định hình vai trò & Chiến lược bù đắp năng lực', subtitle_style))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#2563EB'), spaceAfter=5, spaceBefore=0))

    story.append(Paragraph('<b>1. Lựa chọn Mô hình Tổ chức: Embedded Model (Nhúng trực tiếp)</b>', h2_style))
    arch_text = '''
    • <b>Lý do chọn Embedded:</b> Nhóm có 3 thành viên đang phát triển sản phẩm đơn lẻ từ giai đoạn đầu (0 to 1). Mô hình nhúng trực tiếp giúp Kỹ sư AI, Backend và Quản lý sản phẩm ngồi sát nhau, trao đổi trực tiếp hàng ngày và sửa lỗi ngay khi nhận phản hồi từ bếp ăn.<br/>
    • <b>Tránh lãng phí:</b> Không chọn Centralized (chỉ hợp công ty nhiều sản phẩm) hay Hybrid (phù hợp khi team 20+ người).
    '''
    story.append(Paragraph(arch_text, body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>2. Định hình Vai trò Cốt lõi (Hiện tại) & Mở rộng (Tương lai)</b>', h2_style))
    roles_data = [
        [
            Paragraph('<b>CORE ROLES (Năng lực cốt lõi — Cần ngay cho MVP)</b>', table_cell_bold),
            Paragraph('<b>EXTENDED ROLES (Năng lực mở rộng — Khi scale 10+ trường)</b>', table_cell_bold)
        ],
        [
            Paragraph('''
            • <b>Đỗ Tú Anh (Product Owner & User Researcher):</b> Đi thực tế khảo sát bếp ăn, quản lý tiến độ, điều phối nguồn lực.<br/>
            • <b>Trần Thanh Huyền (Lead AI / LLM Engineer):</b> Xây dựng pipeline RAG, viết prompt, thiết lập guardrails chặn lỗi dị ứng.<br/>
            • <b>Thiều Thị Ngọc Ánh (Data, Backend & QA):</b> Dọn dẹp dữ liệu dinh dưỡng, viết API kết nối web, vận hành bộ test.
            ''', table_cell),
            Paragraph('''
            • <b>MLOps & Observability Engineer:</b> Giám sát độ trôi dữ liệu (data drift), tối ưu độ trễ và chi phí token API khi nhiều trường truy cập cùng lúc.<br/>
            • <b>Legal & Compliance Specialist:</b> Rà soát hợp đồng B2B trường học, đảm bảo tuân thủ Luật An toàn Thực phẩm và bảo mật dữ liệu học sinh.
            ''', table_cell)
        ]
    ]
    t_roles = Table(roles_data, colWidths=[260, 263])
    t_roles.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_roles)
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>3. Chiến lược Bổ sung Năng lực còn thiếu (Priority Resourcing)</b>', h2_style))
    p3_res = [
        [Paragraph('<b>Lỗ hổng năng lực (Gap)</b>', table_cell_bold), Paragraph('<b>Chiến lược giải quyết</b>', table_cell_bold), Paragraph('<b>Lý do chọn phương án này</b>', table_cell_bold), Paragraph('<b>Thời điểm cần</b>', table_cell_bold)],
        [
            Paragraph('<b>Chuyên môn Dinh dưỡng Nhi & Y tế</b><br/>(Định mức RNI, dị ứng chéo)', table_cell),
            Paragraph('🤝 <b>PARTNER</b><br/>(Hợp tác Chuyên gia)', table_cell),
            Paragraph('Giai đoạn thử nghiệm chỉ cần bác sĩ xem qua bộ luật và ca khó, <b>không cần quỹ lương full-time</b>. Hợp tác bác sĩ Viện Dinh Dưỡng giúp tăng uy tín.', table_cell),
            Paragraph('<b>Tuần 1</b><br/>(Trước khi đóng bộ dữ liệu)', table_cell)
        ],
        [
            Paragraph('<b>Thiết kế UI/UX Web Bếp ăn</b><br/>(Giao diện màn hình to, dễ bấm)', table_cell),
            Paragraph('💼 <b>OUTSOURCE</b><br/>(Thuê ngoài ngắn hạn)', table_cell),
            Paragraph('Khối lượng thiết kế MVP ít (khoảng 8 màn hình). Thuê Freelancer trọn gói trong 10 ngày giúp tiết kiệm 70% chi phí và xong nhanh.', table_cell),
            Paragraph('<b>Tuần 2–3</b><br/>(Trước khi mang đi demo)', table_cell)
        ],
        [
            Paragraph('<b>Bộ công cụ Tự động Test AI</b><br/>(Chạy test tự động chống sót dị ứng)', table_cell),
            Paragraph('🎯 <b>INTERNAL UPSKILL</b><br/>(Nâng cao nội bộ)', table_cell),
            Paragraph('Đây là <b>năng lực lõi sống còn</b> để đảm bảo an toàn. Kỹ sư AI (Huyền) sẽ tự học thư viện mã nguồn mở để làm chủ công nghệ đo lường.', table_cell),
            Paragraph('<b>Tháng thứ 2</b><br/>(Trước khi mở rộng 3 trường)', table_cell)
        ]
    ]
    t_p3 = Table(p3_res, colWidths=[120, 95, 218, 90])
    t_p3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_p3)
    story.append(Spacer(1, 3))

    story.append(Paragraph('<b>4. Mục tiêu Chung của Nhóm (Squad Goal)</b>', h2_style))
    goal_box = [
        [Paragraph('''
        <b>MỤC TIÊU SQUAD:</b> <i>"Nhóm chúng tôi sở hữu <b>năng lực tích hợp AI RAG với dữ liệu dinh dưỡng y tế chuẩn hóa</b>, chịu trách nhiệm đưa <b>quy trình thẩm định thực đơn bán trú từ chỗ làm tay mất 3 tiếng với nhiều rủi ro sót dị ứng thành một hệ thống tự động kiểm tra chỉ mất dưới 5 giây và phát hiện chính xác 100% các thành phần dị ứng</b>."</i>
        ''', callout_style)]
    ]
    t_goal = Table(goal_box, colWidths=[523])
    t_goal.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F0FDF4')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#16A34A')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_goal)

    story.append(PageBreak())

    # PAGE 4: TEAM HEALTH & GROWTH PLAN
    story.append(Paragraph('ARTEFACT 4: SỨC KHỎE ĐỘI NGŨ & KẾ HOẠCH HÀNH ĐỘNG 30 NGÀY', title_style))
    story.append(Paragraph('Dự án: NutriMenu AI — Tự đánh giá 4 khía cạnh, Nâng cấp L1->L3 & 3 Hành động cụ thể', subtitle_style))
    story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#2563EB'), spaceAfter=5, spaceBefore=0))

    story.append(Paragraph('<b>1. Tự Đánh Giá Sức Khỏe Nhóm (Thang điểm 1–5) & Phân tích Điểm nghẽn</b>', h2_style))
    health_data = [
        [
            Paragraph('<b>Khía cạnh Đánh giá</b>', table_cell_bold),
            Paragraph('<b>Đỗ Tú Anh</b><br/>(PO)', table_cell_center_bold),
            Paragraph('<b>Trần Thanh Huyền</b><br/>(AI)', table_cell_center_bold),
            Paragraph('<b>Thiều Thị Ngọc Ánh</b><br/>(Data/QA)', table_cell_center_bold),
            Paragraph('<b>Điểm TB</b>', table_cell_center_bold),
            Paragraph('<b>Đánh giá thực tế</b>', table_cell_bold)
        ],
        [
            Paragraph('1. Chất lượng AI (Output ổn định, không bịa đặt)', table_cell),
            Paragraph('3 / 5', table_cell_center),
            Paragraph('3 / 5', table_cell_center),
            Paragraph('4 / 5', table_cell_center),
            Paragraph('<b>3.3 / 5</b>', table_cell_center_bold),
            Paragraph('Chạy mẫu tốt nhưng chưa có bộ đo tự động.', table_cell)
        ],
        [
            Paragraph('2. Tiến độ (Hoàn thành đúng cam kết)', table_cell),
            Paragraph('4 / 5', table_cell_center),
            Paragraph('3 / 5', table_cell_center),
            Paragraph('3 / 5', table_cell_center),
            Paragraph('<b>3.3 / 5</b>', table_cell_center_bold),
            Paragraph('Cơ bản đúng hạn nhưng các mốc hơi gấp.', table_cell)
        ],
        [
            Paragraph('3. Tinh thần đồng đội (Cởi mở, an toàn tâm lý)', table_cell),
            Paragraph('4 / 5', table_cell_center),
            Paragraph('4 / 5', table_cell_center),
            Paragraph('5 / 5', table_cell_center),
            Paragraph('<b>4.3 / 5</b>', table_cell_center_bold),
            Paragraph('Rất tốt, phối hợp ăn ý, sẵn sàng hỗ trợ.', table_cell)
        ],
        [
            Paragraph('4. Tốc độ ra sản phẩm (Thời gian từ code đến test)', table_cell),
            Paragraph('3 / 5', table_cell_center),
            Paragraph('2 / 5', table_cell_center),
            Paragraph('3 / 5', table_cell_center),
            Paragraph('<b>2.7 / 5</b>', table_cell_center_bold),
            Paragraph('🔴 <b>Thấp nhất: Điểm nghẽn cần sửa ngay.</b>', table_cell)
        ]
    ]
    t_health = Table(health_data, colWidths=[175, 45, 45, 48, 50, 160])
    t_health.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor('#FEF2F2')),
    ]))
    story.append(t_health)
    story.append(Spacer(1, 2))
    story.append(Paragraph('• <b>Điểm nghẽn cốt lõi:</b> Mỗi lần sửa prompt hay backend, nhóm phải ngồi dò tay lại từng món mất cả buổi chiều khiến tốc độ ra sản phẩm bị chậm (Velocity = 2.7) và dễ bỏ sót lỗi khi demo.', body_style))
    story.append(Spacer(1, 2))

    story.append(Paragraph('<b>2. Nâng cấp Khung Năng lực (Competency Framework L1 -> L3)</b>', h2_style))
    comp_text = '''
    • <b>Thành viên chọn:</b> <b>Trần Thanh Huyền (Lead AI Engineer)</b><br/>
    • <b>Trình độ hiện tại:</b> <b>L2 (AI Practitioner)</b> — Đã thành thạo viết Prompt, dựng pipeline RAG cơ bản và gọi API.<br/>
    • <b>Năng lực cần nâng tiếp theo:</b> 🚀 <b>Tiến lên L3 (AI Builder)</b> — Làm chủ kỹ thuật <b>Tự động đo lường chất lượng AI (Automated LLM Evals)</b>.<br/>
    • <b>Hành động 30 ngày:</b> Soạn bộ <b>50 bài test mẫu</b> (gồm 20 ca dị ứng phức tạp) và viết script tự động chạy chấm điểm mỗi lần push code.
    '''
    story.append(Paragraph(comp_text, body_style))
    story.append(Spacer(1, 2))

    story.append(Paragraph('<b>3. Kế hoạch Hành động Cụ thể trong 30 Ngày Tới (30-Day Growth Plan)</b>', h2_style))
    p4_actions = [
        [
            Paragraph('<b>STT</b>', table_cell_center_bold),
            Paragraph('<b>Vấn đề cần xử lý</b>', table_cell_bold),
            Paragraph('<b>Hành động 30 ngày cụ thể</b>', table_cell_bold),
            Paragraph('<b>Người phụ trách</b>', table_cell_bold),
            Paragraph('<b>Hạn chót</b>', table_cell_bold),
            Paragraph('<b>Dấu hiệu hoàn thành (DoD)</b>', table_cell_bold)
        ],
        [
            Paragraph('1', table_cell_center),
            Paragraph('Mất thời gian test tay, không rõ AI sót lỗi hay không.', table_cell),
            Paragraph('Lập bộ 50 bài test mẫu và viết code `eval_pipeline.py` tự động đo tỷ lệ bắt đúng dị ứng.', table_cell),
            Paragraph('<b>Trần Thanh Huyền</b><br/>(Kỹ sư AI)', table_cell),
            Paragraph('<b>10/09/2026</b>', table_cell),
            Paragraph('Script chạy xuất file `eval_report.json` với <b>tỷ lệ bắt dị ứng >= 99%</b>, không crash.', table_cell)
        ],
        [
            Paragraph('2', table_cell_center),
            Paragraph('Dữ liệu món ăn còn lưu Excel rời, chưa có API.', table_cell),
            Paragraph('Nhập 500 thành phần thực phẩm chuẩn vào DB, viết 3 API chính (quét dị ứng, tính calo, đổi món).', table_cell),
            Paragraph('<b>Thiều Thị Ngọc Ánh</b><br/>(Backend/Data)', table_cell),
            Paragraph('<b>15/09/2026</b>', table_cell),
            Paragraph('100% API pass test, response time < 800ms, có tài liệu Swagger đầy đủ.', table_cell)
        ],
        [
            Paragraph('3', table_cell_center),
            Paragraph('Sợ làm tính năng không đúng thực tế bếp ăn cần.', table_cell),
            Paragraph('Lên lịch họp cố định 30 phút mỗi chiều thứ Sáu để review và lấy góp ý của chú Bếp trưởng trên demo.', table_cell),
            Paragraph('<b>Đỗ Tú Anh</b><br/>(Trưởng nhóm)', table_cell),
            Paragraph('<b>Từ 05/09/2026</b><br/>(4 tuần liền)', table_cell),
            Paragraph('Có đủ 4 biên bản User Feedback Log ghi lại các điểm chỉnh sửa cho tuần sau.', table_cell)
        ]
    ]
    t_p4 = Table(p4_actions, colWidths=[18, 95, 130, 85, 60, 135])
    t_p4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F1F5F9')),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor('#94A3B8')),
        ('INNERGRID', (0,0), (-1,-1), 0.4, colors.HexColor('#E2E8F0')),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_p4)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f'Successfully generated: {filename}')

if __name__ == '__main__':
    build_pdf('Day27_AI-Team-Lab_Team68.pdf')
    build_pdf('Day27_AI-Team Lab_Team68.pdf')
