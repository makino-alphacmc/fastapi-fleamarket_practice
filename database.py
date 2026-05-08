from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declrative_base

# データベースのURLを定義
SQLALCHEMY_DATABASE_URL = "postgresql://fastapiuser:fastapipass@0.0.0:5432/fleamarket"

# データベースのエンジンを作成
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# データベースのセッションを作成するためのクラス
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declrative_base()
# データベースのセッションを取得するための関数
