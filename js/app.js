function scrollToRecommend() {
    document.getElementById("recommend").scrollIntoView({
        behavior: "smooth"
    });
}


const recommendBtn = document.getElementById("recommendBtn");


recommendBtn.addEventListener("click", async function () {

    // =============================
    // 1. 사용자 입력 가져오기
    // =============================

    const major =
        document.getElementById("major").value.trim();

    const grade =
        document.getElementById("grade").value;

    const interest =
        document.getElementById("interest").value.trim();

    const goal =
        document.getElementById("goal").value.trim();

    const concern =
        document.getElementById("concern").value.trim();


    // =============================
    // 2. 필수 입력 확인
    // =============================

    if (major === "") {

        alert("학과를 입력해주세요.");

        document.getElementById("major").focus();

        return;
    }


    if (grade === "") {

        alert("학년을 선택해주세요.");

        document.getElementById("grade").focus();

        return;
    }


    if (interest === "") {

        alert("관심 분야를 입력해주세요.");

        document.getElementById("interest").focus();

        return;
    }


    // =============================
    // 3. 화면 요소
    // =============================

    const loading =
        document.getElementById("loading");

    const result =
        document.getElementById("result");

    const resultContent =
        document.getElementById("resultContent");


    // =============================
    // 4. 로딩 시작
    // =============================

    loading.classList.remove("hidden");

    result.classList.add("hidden");

    recommendBtn.disabled = true;

    recommendBtn.textContent =
        "🤖 AI가 분석하는 중...";


    try {

        // =============================
        // 5. Python API 요청
        // =============================

        const response = await fetch(
            "/api/recommend",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    major: major,

                    grade: grade,

                    interest: interest,

                    goal: goal,

                    concern: concern

                })
            }
        );


        // =============================
        // 6. 서버 응답
        // =============================

        const data =
            await response.json();


        // =============================
        // 7. 오류 확인
        // =============================

        if (!response.ok || !data.success) {

            throw new Error(
                data.message ||
                "AI 추천을 불러오지 못했습니다."
            );
        }


        // =============================
        // 8. AI 결과 표시
        // =============================

        resultContent.innerHTML =
            formatAIResult(data.result);

        result.classList.remove("hidden");


        // 결과 위치로 이동
        result.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });


    } catch (error) {

        console.error(
            "AI 추천 오류:",
            error
        );


        resultContent.innerHTML = `

            <div class="ai-error">

                <h4>
                    😥 AI 추천을 불러오지 못했습니다.
                </h4>

                <p>
                    잠시 후 다시 시도해주세요.
                </p>

            </div>

        `;

        result.classList.remove("hidden");


    } finally {

        // =============================
        // 9. 로딩 종료
        // =============================

        loading.classList.add("hidden");

        recommendBtn.disabled = false;

        recommendBtn.textContent =
            "✨ AI에게 진로 추천받기";

    }

});


// =====================================
// AI 결과 화면 정리
// =====================================

function formatAIResult(text) {

    if (!text) {

        return `
            <p>
                AI가 결과를 생성하지 못했습니다.
            </p>
        `;

    }


    let html = text;


    // ---------------------------------
    // HTML 문자 처리
    // ---------------------------------

    html = html
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");


    // ---------------------------------
    // **굵은 글씨**
    // ---------------------------------

    html = html.replace(
        /\*\*(.*?)\*\*/g,
        "<strong>$1</strong>"
    );


    // ---------------------------------
    // ### 제목
    // ---------------------------------

    html = html.replace(
        /^###\s*(.*)$/gm,
        '<h4 class="ai-heading">$1</h4>'
    );


    // ---------------------------------
    // ## 제목
    // ---------------------------------

    html = html.replace(
        /^##\s*(.*)$/gm,
        '<h3 class="ai-heading">$1</h3>'
    );


    // ---------------------------------
    // 숫자 목록
    // ---------------------------------

    html = html.replace(
        /^(\d+)\.\s+(.*)$/gm,
        `
        <div class="ai-list">

            <span class="ai-number">
                $1
            </span>

            <span>
                $2
            </span>

        </div>
        `
    );


    // ---------------------------------
    // "-" 목록
    // ---------------------------------

    html = html.replace(
        /^[-•]\s+(.*)$/gm,
        `
        <div class="ai-bullet">
            <span>•</span>
            <span>$1</span>
        </div>
        `
    );


    // ---------------------------------
    // 줄바꿈
    // ---------------------------------

    html = html.replace(
        /\n/g,
        "<br>"
    );


    return `

        <div class="ai-result-content">

            ${html}

        </div>

    `;

}