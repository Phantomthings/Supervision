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

@router.get("/api/sequences/seq03")
async def get_seq03_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq03_branch = await opcua.read_variable(VARIABLES["seq03_branch"])
        seq03_ic = await opcua.read_variable(VARIABLES["seq03_ic"])
        seq03_pc = await opcua.read_variable(VARIABLES["seq03_pc"])
        seq03_ready = await opcua.read_variable(VARIABLES["seq03_ready"])
        seq03_fault = await opcua.read_variable(VARIABLES["seq03_fault"])
        
        seq03_start = await opcua.read_variable(VARIABLES["seq03_start"])
        seq03_stop = await opcua.read_variable(VARIABLES["seq03_stop"])
        seq03_ack = await opcua.read_variable(VARIABLES["seq03_ack"])
        
        ready_class = "success" if seq03_ready else "danger"
        fault_class = "danger" if seq03_fault else "success"
        
        start_class = "cmd-btn-active" if seq03_start else "cmd-btn"
        stop_class = "cmd-btn-stop-active" if seq03_stop else "cmd-btn"
        ack_class = "cmd-btn-active" if seq03_ack else "cmd-btn"
        
        html = f"""
        <div class="data-row">
            <span class="label">Step</span>
            <span class="value">{seq03_branch}</span>
        </div>
        <div class="data-row">
            <span class="label">IC</span>
            <span class="value">{seq03_ic}</span>
        </div>
        <div class="data-row">
            <span class="label">PC</span>
            <span class="value">{seq03_pc}</span>
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
            <button class="{start_class}" hx-post="/api/sequences/seq03/start" hx-swap="none">Séquence 03 - Start</button>
            <button class="{stop_class}" hx-post="/api/sequences/seq03/stop" hx-swap="none">Séquence 03 - Stop</button>
            <button class="{ack_class}" hx-post="/api/sequences/seq03/ack" hx-swap="none">Séquence 03 - Ack</button>
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

@router.get("/api/sequences/pdc3")
async def get_pdc3_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq13_ready = await opcua.read_variable(VARIABLES["seq13_ready"])
        seq13_fault = await opcua.read_variable(VARIABLES["seq13_fault"])
        seq13_ic = await opcua.read_variable(VARIABLES["seq13_ic"])
        seq13_pc = await opcua.read_variable(VARIABLES["seq13_pc"])
        seq13_branch = await opcua.read_variable(VARIABLES["seq13_branch"])
        seq13_ack_val = await opcua.read_variable(VARIABLES["seq13_ack"])
        
        hc2p3_current = await opcua.read_variable(VARIABLES["hc2p3_current"])
        hc2p3_voltage = await opcua.read_variable(VARIABLES["hc2p3_voltage"])
        pdc3_plim = await opcua.read_variable(VARIABLES["pdc3_plim"])
        
        evi3_cp_status = await opcua.read_variable(VARIABLES["evi3_cp_status"])
        evi3_substatus = await opcua.read_variable(VARIABLES["evi3_substatus"])
        evi3_error = await opcua.read_variable(VARIABLES["evi3_error"])
        evi3_pilot = await opcua.read_variable(VARIABLES["evi3_pilot"])
        evi3_voltage = await opcua.read_variable(VARIABLES["evi3_voltage"])
        evi3_target_current = await opcua.read_variable(VARIABLES["evi3_target_current"])
        evi3_target_voltage = await opcua.read_variable(VARIABLES["evi3_target_voltage"])
        evi3_soc = await opcua.read_variable(VARIABLES["evi3_soc"])
        
        evi3_start_val = await opcua.read_variable(VARIABLES["evi3_start"])
        evi3_stop_val = await opcua.read_variable(VARIABLES["evi3_stop"])
        evi3_ack_val = await opcua.read_variable(VARIABLES["evi3_ack"])
        evi3_es_val = await opcua.read_variable(VARIABLES["evi3_es"])
        
        evi3_temp1 = await opcua.read_variable(VARIABLES["evi3_temp1"])
        evi3_temp2 = await opcua.read_variable(VARIABLES["evi3_temp2"])
        dcbm3_temp_h = await opcua.read_variable(VARIABLES["dcbm3_temp_h"])
        dcbm3_temp_l = await opcua.read_variable(VARIABLES["dcbm3_temp_l"])
        
        seq13_ready_class = "success" if seq13_ready else "danger"
        seq13_fault_class = "danger" if seq13_fault else "success"
        seq13_ack_class = "cmd-btn-active" if seq13_ack_val else "cmd-btn"
        
        evi3_start_class = "cmd-btn-active" if evi3_start_val else "cmd-btn"
        evi3_stop_class = "cmd-btn-stop-active" if evi3_stop_val else "cmd-btn"
        evi3_ack_class = "cmd-btn-active" if evi3_ack_val else "cmd-btn"
        evi3_es_class = "cmd-btn-active" if evi3_es_val else "cmd-btn"
        
        html = f"""
        <div class="seq-section">
            <h4>Sequence 13</h4>
            <div class="data-row">
                <span class="label">Ready</span>
                <span class="indicator {seq13_ready_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">Fault</span>
                <span class="indicator {seq13_fault_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">IC</span>
                <span class="value">{seq13_ic}</span>
            </div>
            <div class="data-row">
                <span class="label">PC</span>
                <span class="value">{seq13_pc}</span>
            </div>
            <div class="data-row">
                <span class="label">Step</span>
                <span class="value">{seq13_branch}</span>
            </div>
            <div class="cmd-row">
                <button class="{seq13_ack_class}" hx-post="/api/sequences/seq13/ack" hx-swap="none">Séquence 13 - Ack</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>HC2P3</h4>
            <div class="data-row">
                <span class="label">Current Measurement</span>
                <span class="value">{hc2p3_current:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Voltage Measurement</span>
                <span class="value">{hc2p3_voltage:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Limitation de puissance</span>
                <span class="value">{pdc3_plim:.2f}</span>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>EVI3</h4>
            <div class="data-row">
                <span class="label">CP Status Code</span>
                <span class="value">{evi3_cp_status}</span>
            </div>
            <div class="data-row">
                <span class="label">Substate</span>
                <span class="value">{evi3_substatus}</span>
            </div>
            <div class="data-row">
                <span class="label">Error Code</span>
                <span class="value">{evi3_error}</span>
            </div>
            <div class="data-row">
                <span class="label">Pilot Status Code</span>
                <span class="value">{evi3_pilot}</span>
            </div>
            <div class="data-row">
                <span class="label">EVI Voltage Measurement</span>
                <span class="value">{evi3_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Current</span>
                <span class="value">{evi3_target_current}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Voltage</span>
                <span class="value">{evi3_target_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">SOC</span>
                <span class="value">{evi3_soc}%</span>
            </div>
            <div class="cmd-row">
                <button class="{evi3_start_class}" hx-post="/api/sequences/evi3/start" hx-swap="none">EVI - Start</button>
                <button class="{evi3_stop_class}" hx-post="/api/sequences/evi3/stop" hx-swap="none">EVI - Stop</button>
                <button class="{evi3_ack_class}" hx-post="/api/sequences/evi3/ack" hx-swap="none">EVI - Ack</button>
                <button class="{evi3_es_class}" hx-post="/api/sequences/evi3/es" hx-swap="none">EVI - ES</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>Temperature</h4>
            <div class="data-row">
                <span class="label">Temperature du pistolet 1</span>
                <span class="value">{evi3_temp1}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du pistolet 2</span>
                <span class="value">{evi3_temp2}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_H</span>
                <span class="value">{dcbm3_temp_h}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_L</span>
                <span class="value">{dcbm3_temp_l}</span>
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

@router.get("/api/sequences/seq04")
async def get_seq04_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq04_branch = await opcua.read_variable(VARIABLES["seq04_branch"])
        seq04_ic = await opcua.read_variable(VARIABLES["seq04_ic"])
        seq04_pc = await opcua.read_variable(VARIABLES["seq04_pc"])
        seq04_ready = await opcua.read_variable(VARIABLES["seq04_ready"])
        seq04_fault = await opcua.read_variable(VARIABLES["seq04_fault"])
        
        seq04_start = await opcua.read_variable(VARIABLES["seq04_start"])
        seq04_stop = await opcua.read_variable(VARIABLES["seq04_stop"])
        seq04_ack = await opcua.read_variable(VARIABLES["seq04_ack"])
        
        ready_class = "success" if seq04_ready else "danger"
        fault_class = "danger" if seq04_fault else "success"
        
        start_class = "cmd-btn-active" if seq04_start else "cmd-btn"
        stop_class = "cmd-btn-stop-active" if seq04_stop else "cmd-btn"
        ack_class = "cmd-btn-active" if seq04_ack else "cmd-btn"
        
        html = f"""
        <div class="data-row">
            <span class="label">Step</span>
            <span class="value">{seq04_branch}</span>
        </div>
        <div class="data-row">
            <span class="label">IC</span>
            <span class="value">{seq04_ic}</span>
        </div>
        <div class="data-row">
            <span class="label">PC</span>
            <span class="value">{seq04_pc}</span>
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
            <button class="{start_class}" hx-post="/api/sequences/seq04/start" hx-swap="none">Séquence 04 - Start</button>
            <button class="{stop_class}" hx-post="/api/sequences/seq04/stop" hx-swap="none">Séquence 04 - Stop</button>
            <button class="{ack_class}" hx-post="/api/sequences/seq04/ack" hx-swap="none">Séquence 04 - Ack</button>
        </div>
        """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="data-row"><span class="label">Error: {str(e)}</span></div>')

@router.get("/api/sequences/pdc4")
async def get_pdc4_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq23_ready = await opcua.read_variable(VARIABLES["seq23_ready"])
        seq23_fault = await opcua.read_variable(VARIABLES["seq23_fault"])
        seq23_ic = await opcua.read_variable(VARIABLES["seq23_ic"])
        seq23_pc = await opcua.read_variable(VARIABLES["seq23_pc"])
        seq23_branch = await opcua.read_variable(VARIABLES["seq23_branch"])
        seq23_ack_val = await opcua.read_variable(VARIABLES["seq23_ack"])
        
        hc2p4_current = await opcua.read_variable(VARIABLES["hc2p4_current"])
        hc2p4_voltage = await opcua.read_variable(VARIABLES["hc2p4_voltage"])
        pdc4_plim = await opcua.read_variable(VARIABLES["pdc4_plim"])
        
        evi4_cp_status = await opcua.read_variable(VARIABLES["evi4_cp_status"])
        evi4_substatus = await opcua.read_variable(VARIABLES["evi4_substatus"])
        evi4_error = await opcua.read_variable(VARIABLES["evi4_error"])
        evi4_pilot = await opcua.read_variable(VARIABLES["evi4_pilot"])
        evi4_voltage = await opcua.read_variable(VARIABLES["evi4_voltage"])
        evi4_target_current = await opcua.read_variable(VARIABLES["evi4_target_current"])
        evi4_target_voltage = await opcua.read_variable(VARIABLES["evi4_target_voltage"])
        evi4_soc = await opcua.read_variable(VARIABLES["evi4_soc"])
        
        evi4_start_val = await opcua.read_variable(VARIABLES["evi4_start"])
        evi4_stop_val = await opcua.read_variable(VARIABLES["evi4_stop"])
        evi4_ack_val = await opcua.read_variable(VARIABLES["evi4_ack"])
        evi4_es_val = await opcua.read_variable(VARIABLES["evi4_es"])
        
        evi4_temp1 = await opcua.read_variable(VARIABLES["evi4_temp1"])
        evi4_temp2 = await opcua.read_variable(VARIABLES["evi4_temp2"])
        dcbm4_temp_h = await opcua.read_variable(VARIABLES["dcbm4_temp_h"])
        dcbm4_temp_l = await opcua.read_variable(VARIABLES["dcbm4_temp_l"])
        
        seq23_ready_class = "success" if seq23_ready else "danger"
        seq23_fault_class = "danger" if seq23_fault else "success"
        seq23_ack_class = "cmd-btn-active" if seq23_ack_val else "cmd-btn"
        
        evi4_start_class = "cmd-btn-active" if evi4_start_val else "cmd-btn"
        evi4_stop_class = "cmd-btn-stop-active" if evi4_stop_val else "cmd-btn"
        evi4_ack_class = "cmd-btn-active" if evi4_ack_val else "cmd-btn"
        evi4_es_class = "cmd-btn-active" if evi4_es_val else "cmd-btn"
        
        html = f"""
        <div class="seq-section">
            <h4>Sequence 23</h4>
            <div class="data-row">
                <span class="label">Ready</span>
                <span class="indicator {seq23_ready_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">Fault</span>
                <span class="indicator {seq23_fault_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">IC</span>
                <span class="value">{seq23_ic}</span>
            </div>
            <div class="data-row">
                <span class="label">PC</span>
                <span class="value">{seq23_pc}</span>
            </div>
            <div class="data-row">
                <span class="label">Step</span>
                <span class="value">{seq23_branch}</span>
            </div>
            <div class="cmd-row">
                <button class="{seq23_ack_class}" hx-post="/api/sequences/seq23/ack" hx-swap="none">Séquence 23 - Ack</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>HC2P4</h4>
            <div class="data-row">
                <span class="label">Current Measurement</span>
                <span class="value">{hc2p4_current:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Voltage Measurement</span>
                <span class="value">{hc2p4_voltage:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Limitation de puissance</span>
                <span class="value">{pdc4_plim:.2f}</span>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>EVI4</h4>
            <div class="data-row">
                <span class="label">CP Status Code</span>
                <span class="value">{evi4_cp_status}</span>
            </div>
            <div class="data-row">
                <span class="label">Substate</span>
                <span class="value">{evi4_substatus}</span>
            </div>
            <div class="data-row">
                <span class="label">Error Code</span>
                <span class="value">{evi4_error}</span>
            </div>
            <div class="data-row">
                <span class="label">Pilot Status Code</span>
                <span class="value">{evi4_pilot}</span>
            </div>
            <div class="data-row">
                <span class="label">EVI Voltage Measurement</span>
                <span class="value">{evi4_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Current</span>
                <span class="value">{evi4_target_current}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Voltage</span>
                <span class="value">{evi4_target_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">SOC</span>
                <span class="value">{evi4_soc}%</span>
            </div>
            <div class="cmd-row">
                <button class="{evi4_start_class}" hx-post="/api/sequences/evi4/start" hx-swap="none">EVI - Start</button>
                <button class="{evi4_stop_class}" hx-post="/api/sequences/evi4/stop" hx-swap="none">EVI - Stop</button>
                <button class="{evi4_ack_class}" hx-post="/api/sequences/evi4/ack" hx-swap="none">EVI - Ack</button>
                <button class="{evi4_es_class}" hx-post="/api/sequences/evi4/es" hx-swap="none">EVI - ES</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>Temperature</h4>
            <div class="data-row">
                <span class="label">Temperature du pistolet 1</span>
                <span class="value">{evi4_temp1}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du pistolet 2</span>
                <span class="value">{evi4_temp2}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_H</span>
                <span class="value">{dcbm4_temp_h}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_L</span>
                <span class="value">{dcbm4_temp_l}</span>
            </div>
        </div>
        """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="seq-section"><span class="label">Error: {str(e)}</span></div>')

@router.get("/api/sequences/pdc5")
async def get_pdc5_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq14_ready = await opcua.read_variable(VARIABLES["seq14_ready"])
        seq14_fault = await opcua.read_variable(VARIABLES["seq14_fault"])
        seq14_ic = await opcua.read_variable(VARIABLES["seq14_ic"])
        seq14_pc = await opcua.read_variable(VARIABLES["seq14_pc"])
        seq14_branch = await opcua.read_variable(VARIABLES["seq14_branch"])
        seq14_ack_val = await opcua.read_variable(VARIABLES["seq14_ack"])
        
        hc3p5_current = await opcua.read_variable(VARIABLES["hc3p5_current"])
        hc3p5_voltage = await opcua.read_variable(VARIABLES["hc3p5_voltage"])
        pdc5_plim = await opcua.read_variable(VARIABLES["pdc5_plim"])
        
        evi5_cp_status = await opcua.read_variable(VARIABLES["evi5_cp_status"])
        evi5_substatus = await opcua.read_variable(VARIABLES["evi5_substatus"])
        evi5_error = await opcua.read_variable(VARIABLES["evi5_error"])
        evi5_pilot = await opcua.read_variable(VARIABLES["evi5_pilot"])
        evi5_voltage = await opcua.read_variable(VARIABLES["evi5_voltage"])
        evi5_target_current = await opcua.read_variable(VARIABLES["evi5_target_current"])
        evi5_target_voltage = await opcua.read_variable(VARIABLES["evi5_target_voltage"])
        evi5_soc = await opcua.read_variable(VARIABLES["evi5_soc"])
        
        evi5_start_val = await opcua.read_variable(VARIABLES["evi5_start"])
        evi5_stop_val = await opcua.read_variable(VARIABLES["evi5_stop"])
        evi5_ack_val = await opcua.read_variable(VARIABLES["evi5_ack"])
        evi5_es_val = await opcua.read_variable(VARIABLES["evi5_es"])
        
        evi5_temp1 = await opcua.read_variable(VARIABLES["evi5_temp1"])
        evi5_temp2 = await opcua.read_variable(VARIABLES["evi5_temp2"])
        dcbm5_temp_h = await opcua.read_variable(VARIABLES["dcbm5_temp_h"])
        dcbm5_temp_l = await opcua.read_variable(VARIABLES["dcbm5_temp_l"])
        
        seq14_ready_class = "success" if seq14_ready else "danger"
        seq14_fault_class = "danger" if seq14_fault else "success"
        seq14_ack_class = "cmd-btn-active" if seq14_ack_val else "cmd-btn"
        
        evi5_start_class = "cmd-btn-active" if evi5_start_val else "cmd-btn"
        evi5_stop_class = "cmd-btn-stop-active" if evi5_stop_val else "cmd-btn"
        evi5_ack_class = "cmd-btn-active" if evi5_ack_val else "cmd-btn"
        evi5_es_class = "cmd-btn-active" if evi5_es_val else "cmd-btn"
        
        html = f"""
        <div class="seq-section">
            <h4>Sequence 14</h4>
            <div class="data-row">
                <span class="label">Ready</span>
                <span class="indicator {seq14_ready_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">Fault</span>
                <span class="indicator {seq14_fault_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">IC</span>
                <span class="value">{seq14_ic}</span>
            </div>
            <div class="data-row">
                <span class="label">PC</span>
                <span class="value">{seq14_pc}</span>
            </div>
            <div class="data-row">
                <span class="label">Step</span>
                <span class="value">{seq14_branch}</span>
            </div>
            <div class="cmd-row">
                <button class="{seq14_ack_class}" hx-post="/api/sequences/seq14/ack" hx-swap="none">Séquence 14 - Ack</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>HC3P5</h4>
            <div class="data-row">
                <span class="label">Current Measurement</span>
                <span class="value">{hc3p5_current:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Voltage Measurement</span>
                <span class="value">{hc3p5_voltage:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Limitation de puissance</span>
                <span class="value">{pdc5_plim:.2f}</span>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>EVI5</h4>
            <div class="data-row">
                <span class="label">CP Status Code</span>
                <span class="value">{evi5_cp_status}</span>
            </div>
            <div class="data-row">
                <span class="label">Substate</span>
                <span class="value">{evi5_substatus}</span>
            </div>
            <div class="data-row">
                <span class="label">Error Code</span>
                <span class="value">{evi5_error}</span>
            </div>
            <div class="data-row">
                <span class="label">Pilot Status Code</span>
                <span class="value">{evi5_pilot}</span>
            </div>
            <div class="data-row">
                <span class="label">EVI Voltage Measurement</span>
                <span class="value">{evi5_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Current</span>
                <span class="value">{evi5_target_current}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Voltage</span>
                <span class="value">{evi5_target_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">SOC</span>
                <span class="value">{evi5_soc}%</span>
            </div>
            <div class="cmd-row">
                <button class="{evi5_start_class}" hx-post="/api/sequences/evi5/start" hx-swap="none">EVI - Start</button>
                <button class="{evi5_stop_class}" hx-post="/api/sequences/evi5/stop" hx-swap="none">EVI - Stop</button>
                <button class="{evi5_ack_class}" hx-post="/api/sequences/evi5/ack" hx-swap="none">EVI - Ack</button>
                <button class="{evi5_es_class}" hx-post="/api/sequences/evi5/es" hx-swap="none">EVI - ES</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>Temperature</h4>
            <div class="data-row">
                <span class="label">Temperature du pistolet 1</span>
                <span class="value">{evi5_temp1}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du pistolet 2</span>
                <span class="value">{evi5_temp2}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_H</span>
                <span class="value">{dcbm5_temp_h}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_L</span>
                <span class="value">{dcbm5_temp_l}</span>
            </div>
        </div>
        """
        
        return HTMLResponse(html)
    except Exception as e:
        return HTMLResponse(f'<div class="seq-section"><span class="label">Error: {str(e)}</span></div>')

@router.get("/api/sequences/pdc6")
async def get_pdc6_data():
    try:
        from main import get_opcua_client
        opcua = get_opcua_client()
        
        seq24_ready = await opcua.read_variable(VARIABLES["seq24_ready"])
        seq24_fault = await opcua.read_variable(VARIABLES["seq24_fault"])
        seq24_ic = await opcua.read_variable(VARIABLES["seq24_ic"])
        seq24_pc = await opcua.read_variable(VARIABLES["seq24_pc"])
        seq24_branch = await opcua.read_variable(VARIABLES["seq24_branch"])
        seq24_ack_val = await opcua.read_variable(VARIABLES["seq24_ack"])
        
        hc3p6_current = await opcua.read_variable(VARIABLES["hc3p6_current"])
        hc3p6_voltage = await opcua.read_variable(VARIABLES["hc3p6_voltage"])
        pdc6_plim = await opcua.read_variable(VARIABLES["pdc6_plim"])
        
        evi6_cp_status = await opcua.read_variable(VARIABLES["evi6_cp_status"])
        evi6_substatus = await opcua.read_variable(VARIABLES["evi6_substatus"])
        evi6_error = await opcua.read_variable(VARIABLES["evi6_error"])
        evi6_pilot = await opcua.read_variable(VARIABLES["evi6_pilot"])
        evi6_voltage = await opcua.read_variable(VARIABLES["evi6_voltage"])
        evi6_target_current = await opcua.read_variable(VARIABLES["evi6_target_current"])
        evi6_target_voltage = await opcua.read_variable(VARIABLES["evi6_target_voltage"])
        evi6_soc = await opcua.read_variable(VARIABLES["evi6_soc"])
        
        evi6_start_val = await opcua.read_variable(VARIABLES["evi6_start"])
        evi6_stop_val = await opcua.read_variable(VARIABLES["evi6_stop"])
        evi6_ack_val = await opcua.read_variable(VARIABLES["evi6_ack"])
        evi6_es_val = await opcua.read_variable(VARIABLES["evi6_es"])
        
        evi6_temp1 = await opcua.read_variable(VARIABLES["evi6_temp1"])
        evi6_temp2 = await opcua.read_variable(VARIABLES["evi6_temp2"])
        dcbm6_temp_h = await opcua.read_variable(VARIABLES["dcbm6_temp_h"])
        dcbm6_temp_l = await opcua.read_variable(VARIABLES["dcbm6_temp_l"])
        
        seq24_ready_class = "success" if seq24_ready else "danger"
        seq24_fault_class = "danger" if seq24_fault else "success"
        seq24_ack_class = "cmd-btn-active" if seq24_ack_val else "cmd-btn"
        
        evi6_start_class = "cmd-btn-active" if evi6_start_val else "cmd-btn"
        evi6_stop_class = "cmd-btn-stop-active" if evi6_stop_val else "cmd-btn"
        evi6_ack_class = "cmd-btn-active" if evi6_ack_val else "cmd-btn"
        evi6_es_class = "cmd-btn-active" if evi6_es_val else "cmd-btn"
        
        html = f"""
        <div class="seq-section">
            <h4>Sequence 24</h4>
            <div class="data-row">
                <span class="label">Ready</span>
                <span class="indicator {seq24_ready_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">Fault</span>
                <span class="indicator {seq24_fault_class}"></span>
            </div>
            <div class="data-row">
                <span class="label">IC</span>
                <span class="value">{seq24_ic}</span>
            </div>
            <div class="data-row">
                <span class="label">PC</span>
                <span class="value">{seq24_pc}</span>
            </div>
            <div class="data-row">
                <span class="label">Step</span>
                <span class="value">{seq24_branch}</span>
            </div>
            <div class="cmd-row">
                <button class="{seq24_ack_class}" hx-post="/api/sequences/seq24/ack" hx-swap="none">Séquence 24 - Ack</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>HC3P6</h4>
            <div class="data-row">
                <span class="label">Current Measurement</span>
                <span class="value">{hc3p6_current:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Voltage Measurement</span>
                <span class="value">{hc3p6_voltage:.2f}</span>
            </div>
            <div class="data-row">
                <span class="label">Limitation de puissance</span>
                <span class="value">{pdc6_plim:.2f}</span>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>EVI6</h4>
            <div class="data-row">
                <span class="label">CP Status Code</span>
                <span class="value">{evi6_cp_status}</span>
            </div>
            <div class="data-row">
                <span class="label">Substate</span>
                <span class="value">{evi6_substatus}</span>
            </div>
            <div class="data-row">
                <span class="label">Error Code</span>
                <span class="value">{evi6_error}</span>
            </div>
            <div class="data-row">
                <span class="label">Pilot Status Code</span>
                <span class="value">{evi6_pilot}</span>
            </div>
            <div class="data-row">
                <span class="label">EVI Voltage Measurement</span>
                <span class="value">{evi6_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Current</span>
                <span class="value">{evi6_target_current}</span>
            </div>
            <div class="data-row">
                <span class="label">Target Voltage</span>
                <span class="value">{evi6_target_voltage}</span>
            </div>
            <div class="data-row">
                <span class="label">SOC</span>
                <span class="value">{evi6_soc}%</span>
            </div>
            <div class="cmd-row">
                <button class="{evi6_start_class}" hx-post="/api/sequences/evi6/start" hx-swap="none">EVI - Start</button>
                <button class="{evi6_stop_class}" hx-post="/api/sequences/evi6/stop" hx-swap="none">EVI - Stop</button>
                <button class="{evi6_ack_class}" hx-post="/api/sequences/evi6/ack" hx-swap="none">EVI - Ack</button>
                <button class="{evi6_es_class}" hx-post="/api/sequences/evi6/es" hx-swap="none">EVI - ES</button>
            </div>
        </div>
        
        <div class="seq-section">
            <h4>Temperature</h4>
            <div class="data-row">
                <span class="label">Temperature du pistolet 1</span>
                <span class="value">{evi6_temp1}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du pistolet 2</span>
                <span class="value">{evi6_temp2}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_H</span>
                <span class="value">{dcbm6_temp_h}</span>
            </div>
            <div class="data-row">
                <span class="label">Temperature du DCBM_L</span>
                <span class="value">{dcbm6_temp_l}</span>
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
