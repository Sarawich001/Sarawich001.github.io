import csv

def create_applicant_form():
    """
    สร้างแบบฟอร์มรับสมัครและบันทึกข้อมูลลงในไฟล์ .csv
    """
    print("--- แบบฟอร์มการรับสมัคร ---")
    
    # รับข้อมูลจากผู้ใช้
    full_name = input("กรุณาใส่ชื่อ-นามสกุล: ")
    phone_number = input("กรุณาใส่หมายเลขโทรศัพท์: ")
    team_name = input("กรุณาใส่ชื่อทีม: ")

    # ข้อมูลที่จะบันทึกลงในไฟล์
    applicant_data = [full_name, phone_number, team_name]

    # ชื่อไฟล์ CSV
    filename = 'applicants.csv'
    
    try:
        # เปิดไฟล์ในโหมด 'a' (append) เพื่อเพิ่มข้อมูลต่อท้าย
        # newline='' เพื่อป้องกันการเกิดบรรทัดว่าง
        # encoding='utf-8' เพื่อรองรับภาษาไทย
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # ตรวจสอบว่าไฟล์มีหัวข้อแล้วหรือยัง
            # ถ้าไฟล์ยังไม่มีข้อมูล ให้เขียนหัวข้อก่อน
            try:
                if file.tell() == 0:
                    writer.writerow(["ชื่อ-นามสกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])
            except:
                 writer.writerow(["ชื่อ-นามสกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])

            # เขียนข้อมูลผู้สมัครลงในไฟล์
            writer.writerow(applicant_data)
            
        print(f"\nบันทึกข้อมูลเรียบร้อยแล้วในไฟล์ '{filename}'")
        print(f"ข้อมูลที่บันทึก: {applicant_data}")
        
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")

if __name__ == "__main__":
    create_applicant_form()
