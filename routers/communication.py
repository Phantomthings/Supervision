from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from config import VARIABLES

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/communication", response_class=HTMLResponse)
async def communication_page(request: Request):
    return templates.TemplateResponse("communication.html", {"request": request})

@router.get("/api/communication")
async def get_communication():
    try:
        from main import get_opcua_client
        opcua_client = get_opcua_client()
        
        comm_vars = {
            "RIO": await opcua_client.read_variable(VARIABLES["rio_comflt"]),
            "HC1": await opcua_client.read_variable(VARIABLES["hc1_comflt"]),
            "HC2": await opcua_client.read_variable(VARIABLES["hc2_comflt"]),
            "HC3": await opcua_client.read_variable(VARIABLES["hc3_comflt"]),
            "HMI - PDC12": await opcua_client.read_variable(VARIABLES["hmi_c1_comflt"]),
            "HMI - PDC34": await opcua_client.read_variable(VARIABLES["hmi_c2_comflt"]),
            "HMI - PDC56": await opcua_client.read_variable(VARIABLES["hmi_c3_comflt"]),
            "EVI - PDC1": await opcua_client.read_variable(VARIABLES["evi_p1_comok"]),
            "EVI - PDC2": await opcua_client.read_variable(VARIABLES["evi_p2_comok"]),
            "EVI - PDC3": await opcua_client.read_variable(VARIABLES["evi_p3_comok"]),
            "EVI - PDC4": await opcua_client.read_variable(VARIABLES["evi_p4_comok"]),
            "EVI - PDC5": await opcua_client.read_variable(VARIABLES["evi_p5_comok"]),
            "EVI - PDC6": await opcua_client.read_variable(VARIABLES["evi_p6_comok"]),
            "OCPP - PDC1/PDC2": await opcua_client.read_variable(VARIABLES["ocpp_pdc12_ok"]),
            "OCPP - PDC3/PDC4": await opcua_client.read_variable(VARIABLES["ocpp_pdc34_ok"]),
            "OCPP - PDC5/PDC6": await opcua_client.read_variable(VARIABLES["ocpp_pdc56_ok"]),
            "BESS": await opcua_client.read_variable(VARIABLES["bess_comflt"]),
            "DCBM 1": await opcua_client.read_variable(VARIABLES["dcbm1_comflt"]),
            "DCBM 2": await opcua_client.read_variable(VARIABLES["dcbm2_comflt"]),
            "DCBM 3": await opcua_client.read_variable(VARIABLES["dcbm3_comflt"]),
            "DCBM 4": await opcua_client.read_variable(VARIABLES["dcbm4_comflt"]),
            "DCBM 5": await opcua_client.read_variable(VARIABLES["dcbm5_comflt"]),
            "DCBM 6": await opcua_client.read_variable(VARIABLES["dcbm6_comflt"]),
        }
        
        inverted_logic = ["EVI - PDC1", "EVI - PDC2", "EVI - PDC3", "EVI - PDC4", "EVI - PDC5", "EVI - PDC6", 
                          "OCPP - PDC1/PDC2", "OCPP - PDC3/PDC4", "OCPP - PDC5/PDC6"]
        
        html = ""
        for label, value in comm_vars.items():
            if label in inverted_logic:
                status_class = "success" if value else "danger"
            else:
                status_class = "danger" if value else "success"
            
            html += f"""
            <div class="comm-item">
                <span class="comm-label">{label}</span>
                <span class="indicator {status_class}"></span>
            </div>
            """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="comm-item"><span class="comm-label">Error: {str(e)}</span></div>')