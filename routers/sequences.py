import asyncio
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from config import VARIABLES

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/sequences", response_class=HTMLResponse)
async def sequences_page(request: Request):
    return templates.TemplateResponse("sequences.html", {"request": request})

@router.get("/api/sequences/seq02")
async def get_seq02_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq02_branch = await opcua.read_variable(VARIABLES["seq02_branch"])
        seq02_ic = await opcua.read_variable(VARIABLES["seq02_ic"])
        seq02_pc = await opcua.read_variable(VARIABLES["seq02_pc"])
        seq02_ready = await opcua.read_variable(VARIABLES["seq02_ready"])
        seq02_fault = await opcua.read_variable(VARIABLES["seq02_fault"])
        
        seq02_start = await opcua.read_variable(VARIABLES["seq02_start"])
        seq02_stop = await opcua.read_variable(VARIABLES["seq02_stop"])
        seq02_ack = await opcua.read_variable(VARIABLES["seq02_ack"])
        
        ready_class = "success" if seq02_ready else "danger"
        fault_class = "danger" if seq02_fault else "success"
        
        start_class = "cmd-btn-active" if seq02_start else "cmd-btn"
        stop_class = "cmd-btn-stop-active" if seq02_stop else "cmd-btn"
        ack_class = "cmd-btn-active" if seq02_ack else "cmd-btn"
        
        html = f"""
        <div class="data-row">
            <span class="label">Step</span>
            <span class="value">{seq02_branch}</span>
        </div>
        <div class="data-row">
            <span class="label">IC</span>
            <span class="value">{seq02_ic}</span>
        </div>
        <div class="data-row">
            <span class="label">PC</span>
            <span class="value">{seq02_pc}</span>
        </div>
        <div class="data-row">
            <span class="label">Ready</span>
            <span class="indicator {ready_class}"></span>
        </div>
        <div class="data-row">
            <span class="label">Fault</span>
            <span class="indicator {fault_class}"></span>
        </div>
        <div class="cmd-row">
            <button class="{start_class}" hx-post="/api/sequences/seq02/start" hx-swap="none">Séquence 02 - Start</button>
            <button class="{stop_class}" hx-post="/api/sequences/seq02/stop" hx-swap="none">Séquence 02 - Stop</button>
            <button class="{ack_class}" hx-post="/api/sequences/seq02/ack" hx-swap="none">Séquence 02 - Ack</button>
        </div>
        """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="data-row"><span class="label">Error: {str(e)}</span></div>')

@router.get("/api/sequences/pdc1")
async def get_pdc1_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq12_ready = await opcua.read_variable(VARIABLES["seq12_ready"])
        seq12_fault = await opcua.read_variable(VARIABLES["seq12_fault"])
        seq12_ic = await opcua.read_variable(VARIABLES["seq12_ic"])
        seq12_pc = await opcua.read_variable(VARIABLES["seq12_pc"])
        seq12_branch = await opcua.read_variable(VARIABLES["seq12_branch"])
        seq12_ack_val = await opcua.read_variable(VARIABLES["seq12_ack"])
        
        hc1p1_current = await opcua.read_variable(VARIABLES["hc1p1_current"])
        hc1p1_voltage = await opcua.read_variable(VARIABLES["hc1p1_voltage"])
        pdc1_plim = await opcua.read_variable(VARIABLES["pdc1_plim"])
        
        evi1_cp_status = await opcua.read_variable(VARIABLES["evi1_cp_status"])
        evi1_substatus = await opcua.read_variable(VARIABLES["evi1_substatus"])
        evi1_error = await opcua.read_variable(VARIABLES["evi1_error"])
        evi1_pilot = await opcua.read_variable(VARIABLES["evi1_pilot"])
        evi1_voltage = await opcua.read_variable(VARIABLES["evi1_voltage"])
        evi1_target_current = await opcua.read_variable(VARIABLES["evi1_target_current"])
        evi1_target_voltage = await opcua.read_variable(VARIABLES["evi1_target_voltage"])
        evi1_soc = await opcua.read_variable(VARIABLES["evi1_soc"])
        
        evi1_start_val = await opcua.read_variable(VARIABLES["evi1_start"])
        evi1_stop_val = await opcua.read_variable(VARIABLES["evi1_stop"])
        evi1_ack_val = await opcua.read_variable(VARIABLES["evi1_ack"])
        evi1_es_val = await opcua.read_variable(VARIABLES["evi1_es"])
        
        evi1_temp1 = await opcua.read_variable(VARIABLES["evi1_temp1"])
        evi1_temp2 = await opcua.read_variable(VARIABLES["evi1_temp2"])
        dcbm1_temp_h = await opcua.read_variable(VARIABLES["dcbm1_temp_h"])
        dcbm1_temp_l = await opcua.read_variable(VARIABLES["dcbm1_temp_l"])
        
        seq12_ready_class = "success" if seq12_ready else "danger"
        seq12_fault_class = "danger" if seq12_fault else "success"
        seq12_ack_class = "cmd-btn-active" if seq12_ack_val else "cmd-btn"
        
        evi1_start_class = "cmd-btn-active" if evi1_start_val else "cmd-btn"
        evi1_stop_class = "cmd-btn-stop-active" if evi1_stop_val else "cmd-btn"
        evi1_ack_class = "cmd-btn-active" if evi1_ack_val else "cmd-btn"
        evi1_es_class = "cmd-btn-active" if evi1_es_val else "cmd-btn"
        
        html = f"""
        <div class="seq-section">
            <h4>Sequence 12</h4>
            <div class="data-row">
                <span class="label">Ready</span>
                <span class="indicator {seq12_ready_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">Fault</span>
                <span class="indicator {seq12_fault_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">IC</span>
                <span class="value">{seq12_ic}</span>
            </div>
            <div class="data-row">
                <span class="label">PC</span>
                <span class="value">{seq12_pc}</span>
            </div>
            <div class="data-row">
                <span class="label">Step</span>
                <span class="value">{seq12_branch}</span>
            </div>
            <div class="cmd-row">
                <button class="{seq12_ack_class}" hx-post="/api/sequences/seq12/ack" hx-swap="none">Séquence 12 - Ack</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>HC1P1</h4>
            <div class="data-row">
                <span class="label">Current Measurement</span>
                <span class="value">{hc1p1_current:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Voltage Measurement</span>
                <span class="value">{hc1p1_voltage:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Limitation de puissance</span>
                <span class="value">{pdc1_plim:.2f}</span>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>EVI1</h4>
            <div class="data-row">
                <span class="label">CP Status Code</span>
                <span class="value">{evi1_cp_status}</span>
            </div>
            <div class="data-row">
                <span class="label">Substate</span>
                <span class="value">{evi1_substatus}</span>
            </div>
            <div class="data-row">
                <span class="label">Error Code</span>
                <span class="value">{evi1_error}</span>
            </div>
            <div class="data-row">
                <span class="label">Pilot Status Code</span>
                <span class="value">{evi1_pilot}</span>
            </div>
            <div class="data-row">
                <span class="label">EVI Voltage Measurement</span>
                <span class="value">{evi1_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Current</span>
                <span class="value">{evi1_target_current}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Voltage</span>
                <span class="value">{evi1_target_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">SOC</span>
                <span class="value">{evi1_soc}%</span>
            </div>
            <div class="cmd-row">
                <button class="{evi1_start_class}" hx-post="/api/sequences/evi1/start" hx-swap="none">EVI - Start</button>
                <button class="{evi1_stop_class}" hx-post="/api/sequences/evi1/stop" hx-swap="none">EVI - Stop</button>
                <button class="{evi1_ack_class}" hx-post="/api/sequences/evi1/ack" hx-swap="none">EVI - Ack</button>
                <button class="{evi1_es_class}" hx-post="/api/sequences/evi1/es" hx-swap="none">EVI - ES</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>Temperature</h4>
            <div class="data-row">
                <span class="label">Temperature du pistolet 1</span>
                <span class="value">{evi1_temp1}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du pistolet 2</span>
                <span class="value">{evi1_temp2}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_H</span>
                <span class="value">{dcbm1_temp_h}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_L</span>
                <span class="value">{dcbm1_temp_l}</span>
            </div>
        </div>
        """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="seq-section"><span class="label">Error: {str(e)}</span></div>')

@router.get("/api/sequences/pdc2")
async def get_pdc2_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq22_ready = await opcua.read_variable(VARIABLES["seq22_ready"])
        seq22_fault = await opcua.read_variable(VARIABLES["seq22_fault"])
        seq22_ic = await opcua.read_variable(VARIABLES["seq22_ic"])
        seq22_pc = await opcua.read_variable(VARIABLES["seq22_pc"])
        seq22_branch = await opcua.read_variable(VARIABLES["seq22_branch"])
        seq22_ack_val = await opcua.read_variable(VARIABLES["seq22_ack"])
        
        hc1p2_current = await opcua.read_variable(VARIABLES["hc1p2_current"])
        hc1p2_voltage = await opcua.read_variable(VARIABLES["hc1p2_voltage"])
        pdc2_plim = await opcua.read_variable(VARIABLES["pdc2_plim"])
        
        evi2_cp_status = await opcua.read_variable(VARIABLES["evi2_cp_status"])
        evi2_substatus = await opcua.read_variable(VARIABLES["evi2_substatus"])
        evi2_error = await opcua.read_variable(VARIABLES["evi2_error"])
        evi2_pilot = await opcua.read_variable(VARIABLES["evi2_pilot"])
        evi2_voltage = await opcua.read_variable(VARIABLES["evi2_voltage"])
        evi2_target_current = await opcua.read_variable(VARIABLES["evi2_target_current"])
        evi2_target_voltage = await opcua.read_variable(VARIABLES["evi2_target_voltage"])
        evi2_soc = await opcua.read_variable(VARIABLES["evi2_soc"])
        
        evi2_start_val = await opcua.read_variable(VARIABLES["evi2_start"])
        evi2_stop_val = await opcua.read_variable(VARIABLES["evi2_stop"])
        evi2_ack_val = await opcua.read_variable(VARIABLES["evi2_ack"])
        evi2_es_val = await opcua.read_variable(VARIABLES["evi2_es"])
        
        evi2_temp1 = await opcua.read_variable(VARIABLES["evi2_temp1"])
        evi2_temp2 = await opcua.read_variable(VARIABLES["evi2_temp2"])
        dcbm2_temp_h = await opcua.read_variable(VARIABLES["dcbm2_temp_h"])
        dcbm2_temp_l = await opcua.read_variable(VARIABLES["dcbm2_temp_l"])
        
        seq22_ready_class = "success" if seq22_ready else "danger"
        seq22_fault_class = "danger" if seq22_fault else "success"
        seq22_ack_class = "cmd-btn-active" if seq22_ack_val else "cmd-btn"
        
        evi2_start_class = "cmd-btn-active" if evi2_start_val else "cmd-btn"
        evi2_stop_class = "cmd-btn-stop-active" if evi2_stop_val else "cmd-btn"
        evi2_ack_class = "cmd-btn-active" if evi2_ack_val else "cmd-btn"
        evi2_es_class = "cmd-btn-active" if evi2_es_val else "cmd-btn"
        
        html = f"""
        <div class="seq-section">
            <h4>Sequence 22</h4>
            <div class="data-row">
                <span class="label">Ready</span>
                <span class="indicator {seq22_ready_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">Fault</span>
                <span class="indicator {seq22_fault_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">IC</span>
                <span class="value">{seq22_ic}</span>
            </div>
            <div class="data-row">
                <span class="label">PC</span>
                <span class="value">{seq22_pc}</span>
            </div>
            <div class="data-row">
                <span class="label">Step</span>
                <span class="value">{seq22_branch}</span>
            </div>
            <div class="cmd-row">
                <button class="{seq22_ack_class}" hx-post="/api/sequences/seq22/ack" hx-swap="none">Séquence 22 - Ack</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>HC1P2</h4>
            <div class="data-row">
                <span class="label">Current Measurement</span>
                <span class="value">{hc1p2_current:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Voltage Measurement</span>
                <span class="value">{hc1p2_voltage:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Limitation de puissance</span>
                <span class="value">{pdc2_plim:.2f}</span>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>EVI2</h4>
            <div class="data-row">
                <span class="label">CP Status Code</span>
                <span class="value">{evi2_cp_status}</span>
            </div>
            <div class="data-row">
                <span class="label">Substate</span>
                <span class="value">{evi2_substatus}</span>
            </div>
            <div class="data-row">
                <span class="label">Error Code</span>
                <span class="value">{evi2_error}</span>
            </div>
            <div class="data-row">
                <span class="label">Pilot Status Code</span>
                <span class="value">{evi2_pilot}</span>
            </div>
            <div class="data-row">
                <span class="label">EVI Voltage Measurement</span>
                <span class="value">{evi2_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Current</span>
                <span class="value">{evi2_target_current}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Voltage</span>
                <span class="value">{evi2_target_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">SOC</span>
                <span class="value">{evi2_soc}%</span>
            </div>
            <div class="cmd-row">
                <button class="{evi2_start_class}" hx-post="/api/sequences/evi2/start" hx-swap="none">EVI - Start</button>
                <button class="{evi2_stop_class}" hx-post="/api/sequences/evi2/stop" hx-swap="none">EVI - Stop</button>
                <button class="{evi2_ack_class}" hx-post="/api/sequences/evi2/ack" hx-swap="none">EVI - Ack</button>
                <button class="{evi2_es_class}" hx-post="/api/sequences/evi2/es" hx-swap="none">EVI - ES</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>Temperature</h4>
            <div class="data-row">
                <span class="label">Temperature du pistolet 1</span>
                <span class="value">{evi2_temp1}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du pistolet 2</span>
                <span class="value">{evi2_temp2}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_H</span>
                <span class="value">{dcbm2_temp_h}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_L</span>
                <span class="value">{dcbm2_temp_l}</span>
            </div>
        </div>
        """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="seq-section"><span class="label">Error: {str(e)}</span></div>')

async def pulse_ack(variable_name: str):
    from main import get_opcua_client
    opcua = get_opcua_client()
    
    for _ in range(10):
        await opcua.write_variable(variable_name, True)
        await asyncio.sleep(0.1)

async def pulse_startstop(variable_name: str):
    from main import get_opcua_client
    opcua = get_opcua_client()
    
    await opcua.write_variable(variable_name, True)
    await asyncio.sleep(3)
    await opcua.write_variable(variable_name, False)

@router.post("/api/sequences/{seq}/{cmd}")
async def execute_command(seq: str, cmd: str, background_tasks: BackgroundTasks):
    try:
        variable_name = VARIABLES[f"{seq}_{cmd}"]
        
        if cmd in ["ack", "es"]:
            background_tasks.add_task(pulse_ack, variable_name)
        else:
            background_tasks.add_task(pulse_startstop, variable_name)
        
        return {"status": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))