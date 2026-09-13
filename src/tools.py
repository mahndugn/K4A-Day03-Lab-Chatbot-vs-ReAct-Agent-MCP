"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu thông tin hồ sơ và số ngày phép nhân viên VinFast
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ thông tin nhân sự VinFast: họ tên, khối phòng ban, chức vụ, cán bộ HR phụ trách và số ngày phép còn lại bằng mã nhân viên (ví dụ: 'VF2026001').",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên VinFast cần tra cứu (ví dụ: 'VF2026001')"
                },
                "student_id": {
                    "type": "string",
                    "description": "Mã định danh nhân viên hoặc sinh viên dự phòng (ví dụ: 'VF2026001' hoặc 'SV2026001')"
                }
            },
            "required": ["employee_id"]
        }
    },
    
    # --------------------------------------------------------------------------
    # [TASK 1.2 - HOÀN THIỆN] TOOL SCHEMA CHO 'schedule_appointment' (VinFast HR)
    # --------------------------------------------------------------------------
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn làm việc hoặc tư vấn chính sách nhân sự, bảo hiểm, chế độ ngày phép với Cán bộ / Chuyên viên Ban Nhân sự VinFast.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên VinFast cần đặt lịch (ví dụ: 'VF2026001')"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn làm việc (ví dụ: '09:00 15/09/2026')"
                },
                "hr_officer": {
                    "type": "string",
                    "description": "Tên chuyên viên hoặc cán bộ nhân sự phụ trách cuộc hẹn (ví dụ: 'Trần Thị Mai - Ban Nhân sự VinFast')"
                },
                "purpose": {
                    "type": "string",
                    "description": "Mục đích buổi làm việc (ví dụ: 'Tư vấn chế độ bảo hiểm sức khỏe', 'Giải quyết ngày phép', 'Thủ tục thâm niên')"
                }
            },
            "required": ["employee_id", "datetime_str"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    # Dữ liệu nhân viên VinFast (Chủ đề 2.1 - Trợ lý Nhân sự VinFast)
    "VF2026001": {
        "full_name": "Nguyễn Văn An",
        "department": "Khối Sản xuất Ô tô điện VinFast Hải Phòng",
        "role": "Kỹ sư Tự động hóa",
        "leave_balance": 12,
        "email": "an.nv@vinfast.vn",
        "status": "Chính thức",
        "hr_officer": "Trần Thị Mai - Ban Nhân sự VinFast"
    },
    "VF2026002": {
        "full_name": "Trần Thị Bình",
        "department": "Khối R&D Pin xe điện VinFast",
        "role": "Chuyên viên R&D",
        "leave_balance": 10,
        "email": "binh.tt@vinfast.vn",
        "status": "Chính thức",
        "hr_officer": "Lê Hoàng Nam - Ban Nhân sự VinFast"
    },
    # Dữ liệu dự phòng sinh viên VinUni mẫu
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
    },
    "SV2026002": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "gpa": 3.60,
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B"
    }
}


def execute_academic_query(student_id: str = None, employee_id: str = None) -> str:
    """Thực thi tra cứu thông tin nhân viên VinFast (hoặc hồ sơ học vụ dự phòng)"""
    target_id = (employee_id or student_id or "").strip().upper()
    record = MOCK_DATABASE.get(target_id)
    if record:
        return json.dumps({
            "status": "SUCCESS",
            "employee_id": target_id,
            "student_id": target_id,
            "data": record
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu nhân viên / hồ sơ có mã '{target_id}'"
        }, ensure_ascii=False)


def execute_schedule_appointment(
    employee_id: str = None,
    student_id: str = None,
    datetime_str: str = "",
    hr_officer: str = None,
    advisor_name: str = None,
    purpose: str = "Tư vấn chính sách nhân sự"
) -> str:
    """Thực thi đặt lịch hẹn làm việc với Ban Nhân sự VinFast"""
    target_id = (employee_id or student_id or "VF2026001").strip().upper()
    officer = hr_officer or advisor_name or "Ban Nhân sự VinFast"
    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{target_id}-99",
        "employee_id": target_id,
        "student_id": target_id,
        "datetime": datetime_str,
        "hr_officer": officer,
        "advisor": officer,
        "purpose": purpose,
        "message": f"Đặt lịch thành công cho nhân viên {target_id} làm việc với {officer} vào lúc {datetime_str} (Mục đích: {purpose})."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "schedule_appointment": execute_schedule_appointment
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
