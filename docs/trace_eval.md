# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Điền Họ và Tên của bạn]  
> **Mã Sinh Viên / Mã Học viên:** [Điền MSSV của bạn]  
> **Chủ đề Lựa chọn:** Gợi ý 2.1 — Trợ lý Nhân sự VinFast (VinFast HR Assistant)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | **4 / 5** | Khi nhân viên yêu cầu kiểm tra cán bộ HR phụ trách rồi mới đặt lịch hẹn, Agent phải chia nhỏ 2 bước suy luận ReAct nối tiếp: (1) tra cứu hồ sơ nhân sự $\rightarrow$ (2) lấy tên cán bộ HR để đặt lịch làm việc. |
| **2. Tool Interaction** | **5 / 5** | Hệ thống bắt buộc phải tương tác với MCP Server để truy vấn dữ liệu hồ sơ nhân sự/ngày phép và phát sinh mã đặt lịch `BK-...`, LLM thuần túy không thể tự biết. |
| **3. Dynamic Decision** | **4 / 5** | Bước tiếp theo phụ thuộc hoàn toàn vào kết quả quan sát bước trước: Nếu mã nhân viên không tồn tại (`NOT_FOUND`), Agent dừng lại báo lỗi lịch sự; nếu tìm thấy hồ sơ thì mới tiếp tục tiến trình. |
| **4. Long Horizon Goal** | **3 / 5** | Hệ thống duy trì mục tiêu giải quyết trọn vẹn yêu cầu của nhân viên từ khâu tra cứu, xử lý lịch hẹn đến xuất câu trả lời tổng hợp cuối cùng. |
| **TỔNG ĐIỂM AGENTIC FIT** | **16 / 20** | *Tổng điểm 16/20 (> 12/20): Bài toán rất phù hợp triển khai hệ thống ReAct Agent.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
