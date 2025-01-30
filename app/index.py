from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [{"name":"ll3YG","marks":52},{"name":"8V","marks":86},{"name":"jQL9kU","marks":95},{"name":"CsfXVlBx","marks":4},{"name":"gzSWHrWzhl","marks":50},{"name":"iml","marks":61},{"name":"Jf5g","marks":67},{"name":"c35","marks":67},{"name":"GY5BGOT","marks":31},{"name":"z","marks":6},{"name":"Z","marks":81},{"name":"Qe3wJJ","marks":73},{"name":"P","marks":98},{"name":"S1qoO","marks":15},{"name":"e0Ng","marks":56},{"name":"lgYm","marks":29},{"name":"05TXYO","marks":45},{"name":"av23E","marks":81},{"name":"XJB4","marks":66},{"name":"gkBS9v","marks":30},{"name":"N04QHNsuG8","marks":20},{"name":"Z45zTZP","marks":55},{"name":"CeE","marks":7},{"name":"gjZ1w","marks":23},{"name":"gdvPI","marks":96},{"name":"Xs","marks":57},{"name":"jnSuGk","marks":39},{"name":"QzR6Pd","marks":92},{"name":"3UE","marks":50},{"name":"V7ud","marks":46},{"name":"yjCZ","marks":45},{"name":"HVHjpN4lWK","marks":15},{"name":"H40gvp7cdc","marks":53},{"name":"wMTNiCH5","marks":13},{"name":"MIQdkMiu","marks":0},{"name":"6t","marks":94},{"name":"Jyf","marks":36},{"name":"aJ","marks":84},{"name":"qJKP","marks":87},{"name":"ef","marks":5},{"name":"qwJfEY","marks":38},{"name":"fr","marks":36},{"name":"JKExqLQ0P","marks":45},{"name":"zKblKR","marks":16},{"name":"Rs3","marks":29},{"name":"C6bsVpIsV","marks":77},{"name":"58CcTp","marks":17},{"name":"T0VAd1V","marks":82},{"name":"hUGTcge2JC","marks":78},{"name":"QVqFE9s0gu","marks":98},{"name":"fYrJ","marks":44},{"name":"FJHkZa6r8V","marks":30},{"name":"a","marks":87},{"name":"F","marks":85},{"name":"8i","marks":3},{"name":"QzHx","marks":42},{"name":"E3Mc4630dV","marks":64},{"name":"OohliAQnaY","marks":21},{"name":"E","marks":98},{"name":"0D","marks":38},{"name":"hJi3C5H","marks":77},{"name":"biy7cOENQk","marks":95},{"name":"2jIof58RvL","marks":4},{"name":"Iu","marks":43},{"name":"SZ","marks":76},{"name":"Oi3w","marks":4},{"name":"q","marks":64},{"name":"gv87","marks":28},{"name":"V","marks":0},{"name":"vEuao","marks":69},{"name":"edONNK","marks":45},{"name":"Oxfkag","marks":12},{"name":"4","marks":16},{"name":"CXngc","marks":47},{"name":"1J","marks":41},{"name":"no","marks":48},{"name":"QQZkGu10RQ","marks":46},{"name":"4Hmv","marks":60},{"name":"MZ4G","marks":77},{"name":"Xm4","marks":2},{"name":"Whr","marks":90},{"name":"zv","marks":3},{"name":"J","marks":77},{"name":"DOnXWd3Xn","marks":28},{"name":"SL6N","marks":89},{"name":"w9Cm","marks":64},{"name":"rMsR","marks":80},{"name":"eQnl9QU","marks":75},{"name":"jp","marks":2},{"name":"xpRuZ03K2W","marks":21},{"name":"qeWEKtjN","marks":65},{"name":"g","marks":79},{"name":"RffUopP","marks":62},{"name":"8xe8","marks":74},{"name":"glxy","marks":8},{"name":"cMZR","marks":20},{"name":"Lm","marks":53},{"name":"iOv5hK","marks":20},{"name":"FnSkKx","marks":64},{"name":"Z","marks":97}]

@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [next((s["marks"] for s in students_data if s["name"] == n), None) for n in name]
        return {"marks": marks}
    return {"marks": []}
