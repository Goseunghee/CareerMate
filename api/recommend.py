import json
import os
from http.server import BaseHTTPRequestHandler

from google import genai


class handler(BaseHTTPRequestHandler):

    # =====================================
    # POST 요청 처리
    # =====================================

    def do_POST(self):

        try:

            # ---------------------------------
            # 1. 요청 데이터 받기
            # ---------------------------------

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            data = json.loads(
                body.decode("utf-8")
            )


            # ---------------------------------
            # 2. 사용자 입력 가져오기
            # ---------------------------------

            major = data.get(
                "major",
                ""
            ).strip()

            grade = data.get(
                "grade",
                ""
            ).strip()

            interest = data.get(
                "interest",
                ""
            ).strip()

            goal = data.get(
                "goal",
                ""
            ).strip()

            concern = data.get(
                "concern",
                ""
            ).strip()


            # ---------------------------------
            # 3. 필수 입력 확인
            # ---------------------------------

            if not major:

                self.send_json(
                    400,
                    {
                        "success": False,
                        "message": "학과를 입력해주세요."
                    }
                )

                return


            if not grade:

                self.send_json(
                    400,
                    {
                        "success": False,
                        "message": "학년을 선택해주세요."
                    }
                )

                return


            if not interest:

                self.send_json(
                    400,
                    {
                        "success": False,
                        "message": "관심 분야를 입력해주세요."
                    }
                )

                return


            # ---------------------------------
            # 4. Gemini API 키 가져오기
            # ---------------------------------

            api_key = os.environ.get(
                "GEMINI_API_KEY"
            )


            if not api_key:

                self.send_json(
                    500,
                    {
                        "success": False,
                        "message":
                            "GEMINI_API_KEY 환경변수가 설정되지 않았습니다."
                    }
                )

                return


            # ---------------------------------
            # 5. Gemini 클라이언트 생성
            # ---------------------------------

            client = genai.Client(
                api_key=api_key
            )


            # ---------------------------------
            # 6. AI 프롬프트
            # ---------------------------------

            prompt = f"""
당신은 대학생의 진로와 취업 준비를 도와주는
전문 진로 상담 AI입니다.

사용자의 정보를 바탕으로 개인에게 맞는
진로 방향과 취업 준비 방법을 친절하고
구체적으로 추천해주세요.

[사용자 정보]

학과: {major}
학년: {grade}
관심 분야: {interest}
희망 진로: {goal if goal else "아직 정하지 못함"}
현재 고민: {concern if concern else "특별히 입력하지 않음"}

다음 내용을 반드시 포함해주세요.

1. 추천 직무 3개
2. 각 직무를 추천하는 이유
3. 필요한 핵심 역량
4. 대학생 때 해보면 좋은 활동
5. 도움이 될 수 있는 자격증이나 학습 분야
6. 현재 학년을 기준으로 한 취업 준비 방향
7. 지금 당장 해볼 수 있는 행동 3가지

답변은 대학생이 이해하기 쉽게 작성해주세요.

특정 기업의 채용 여부나 특정 자격증의
최신 시험 일정처럼 실시간 확인이 필요한
정보는 사실처럼 단정하지 말고 공식 사이트에서
확인하도록 안내해주세요.
"""


            # ---------------------------------
            # 7. Gemini API 호출
            # ---------------------------------

            response = client.models.generate_content(

                model="gemini-3.6-flash",

                contents=prompt

            )


            # ---------------------------------
            # 8. AI 결과 가져오기
            # ---------------------------------

            result_text = response.text


            # ---------------------------------
            # 9. 결과 반환
            # ---------------------------------

            self.send_json(
                200,
                {
                    "success": True,
                    "result": result_text
                }
            )


        except Exception as e:

            # ---------------------------------
            # 오류 출력
            # ---------------------------------

            print(
                "AI API 오류:",
                str(e)
            )


            self.send_json(
                500,
                {
                    "success": False,
                    "message":
                        "AI API 오류: " + str(e)
                }
            )


    # =====================================
    # JSON 응답 함수
    # =====================================

    def send_json(
        self,
        status_code,
        data
    ):

        response = json.dumps(
            data,
            ensure_ascii=False
        ).encode("utf-8")


        self.send_response(
            status_code
        )


        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )


        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )


        self.send_header(
            "Access-Control-Allow-Methods",
            "POST, OPTIONS"
        )


        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )


        self.end_headers()


        self.wfile.write(
            response
        )


    # =====================================
    # OPTIONS 요청 처리
    # =====================================

    def do_OPTIONS(self):

        self.send_response(200)

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.send_header(
            "Access-Control-Allow-Methods",
            "POST, OPTIONS"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )

        self.end_headers()