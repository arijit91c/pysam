class Controls(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	control_mode = float
	dt_hr = float
	input_current = float
	input_power = float


class ParamsCell(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	C_rate = float
	Qexp = float
	Qfull = float
	Qfull_flow = float
	Qnom = float
	Vexp = float
	Vfull = float
	Vnom = float
	Vnom_default = float
	calendar_a = float
	calendar_b = float
	calendar_c = float
	calendar_choice = float
	calendar_matrix = tuple
	calendar_q0 = float
	chem = float
	cycling_matrix = tuple
	initial_SOC = float
	leadacid_q10 = float
	leadacid_q20 = float
	leadacid_qn = float
	leadacid_tn = float
	maximum_SOC = float
	minimum_SOC = float
	resistance = float
	voltage_choice = float
	voltage_matrix = tuple


class ParamsPack(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	Cp = float
	T_room_init = float
	cap_vs_temp = tuple
	h = float
	loss_choice = float
	mass = float
	monthly_charge_loss = tuple
	monthly_discharge_loss = tuple
	monthly_idle_loss = tuple
	nominal_energy = float
	nominal_voltage = float
	replacement_capacity = float
	replacement_option = float
	replacement_schedule_percent = tuple
	schedule_loss = tuple
	surface_area = float


class StatePack(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	I = float
	I_chargeable = float
	I_dischargeable = float
	P = float
	P_chargeable = float
	P_dischargeable = float
	Q = float
	Q_max = float
	SOC = float
	T_batt = float
	T_room = float
	V = float
	heat_dissipated = float
	indices_replaced = tuple
	last_idx = float
	loss_kw = float
	n_replacements = float


class StateCell(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass


	I_loss = float
	SOC_prev = float
	T_batt_prev = float
	average_range = float
	cell_current = float
	cell_voltage = float
	chargeChange = float
	charge_mode = float
	day_age_of_battery = float
	dq_relative_calendar_old = float
	n_cycles = float
	prev_charge = float
	q0 = float
	q1_0 = float
	q2 = float
	q2_0 = float
	q_relative = float
	q_relative_calendar = float
	q_relative_cycle = float
	q_relative_thermal = float
	qmax_lifetime = float
	qmax_thermal = float
	qn = float
	rainflow_Xlt = float
	rainflow_Ylt = float
	rainflow_jlt = float
	rainflow_peaks = tuple
	range = float


class Outputs(object):
	def assign(self): 
		pass

	def export(self) -> dict:
		pass

	def __init__(self, *args, **kwargs): 
		pass




class BatteryStateful(object):
	def assign(self, dict):
		pass

	def value(self, name, value=None):
		pass

	def execute(self, int_verbosity):
		pass

	def export(self):
		pass

	def __getattribute__(self, *args, **kwargs):
		pass

	def __init__(self, *args, **kwargs):
		pass

	Controls = Controls
	ParamsCell = ParamsCell
	ParamsPack = ParamsPack
	StatePack = StatePack
	StateCell = StateCell
	Outputs = Outputs


def default(config) -> BatteryStateful:
	pass

def new() -> BatteryStateful:
	pass

def wrap(ssc_data_t) -> BatteryStateful:
	pass

def from_existing(model, config="") -> BatteryStateful:
	pass

__loader__ = None 

__spec__ = None
