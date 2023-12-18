from fastapi import APIRouter
from dto.commentReqDto import CommentReqDto
from dto.itemImgReqDto import ItemImgReqDto
import kobert
import yolov8

api = APIRouter()

@api.post("/check-malicious-comment")
def checkMaliciousComment(commentReqDto : CommentReqDto):
    # TODO : Call cleanBot Metho
    return kobert.predict(commentReqDto.comment)

@api.post("/check-item-color")
def checkMaliciousComment(itemImgReqDto : ItemImgReqDto):
    # TODO : Call cleanBot Method
    return yolov8.detect_color(itemImgReqDto.itemImgUrl)
