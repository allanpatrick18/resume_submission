import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
from puzzle_solver import solve_puzzle
app = FastAPI()

from database import query_answer


@app.get("/")
async def server():
    return {"msg": "Sever Up!"}

"""
Resume Submission API
"""

@app.get("/submission", response_class=PlainTextResponse, status_code=200)
async def submission(request: Request):
    params = dict(request.query_params)
    if params['q'] == 'Puzzle':
        return solve_puzzle((params['d']))
    result = query_answer(params['q'])
    return result


def log_questions(params: dict):
    """
    Create a file with the parameters of request
    :param params: {'q':'resume', 'd': 'description'}
    :return: None
    """
    params = f"'{params['q']}','{params['d']}', "
    f = open("parameters.csv", "a")
    f.write(params)
    f.write('\n')
    f.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)