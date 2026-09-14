from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# إنشاء التطبيق
app = FastAPI(title="Knowledge Graph API")

# إعداد CORS باش الفرونت-اند (HTML/JS) يقدر يتواصل مع السيرفر بلا مشاكل (CORS Error)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # فمرحلة التطوير كنخليوها مفتوحة
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# مسار بسيط باش نتأكدو بلي السيرفر خدام
@app.get("/")
def read_root():
    return {"message": "السيرفر خدام مزيان! 🚀"}

# مسار (Endpoint) وهمي حاليا باش نستقبلو الـ PDF (غنعمروه فالخطوة الجاية)
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "تم استقبال الملف بنجاح! (التحليل غنزيدوه فالخطوة الجاية)"
    }