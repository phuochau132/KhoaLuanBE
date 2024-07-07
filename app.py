from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.UserController import user_router
from controller.PredictController import predict_router
app = FastAPI()
# Cấu hình middleware CORS để cho phép các yêu cầu từ nguồn gốc khác nhau
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
)
# Đăng ký các router
app.include_router(user_router, prefix="/users")
app.include_router(predict_router, prefix="/predict")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
