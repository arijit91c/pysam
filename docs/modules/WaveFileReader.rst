.. _WaveFileReader:

WaveFileReader
***********************************

Wrapper for SAM Simulation Core model: `cmod_wave_file_reader.cpp <https://github.com/NREL/ssc/blob/develop/ssc/cmod_wave_file_reader.cpp>`_

Input Consistency Warning
==================================

As described in :ref:`Possible Problems <possible_problems>`, some input parameters are interdependent but the equations 
that enforce consistency are not available in this PySAM module. Therefore,
the onus is on the PySAM user to check that interdependencies are correctly handled. The variables which may require
additional logic include:


Provided for each of these inputs is a list of other inputs that are potentially interdependent. 

Creating an Instance
===================================

Refer to the :ref:`Initializing a Model <initializing>` page for details on the different ways to create an instance of a PySAM class.

**WaveFileReader model description**

.. automodule:: PySAM.WaveFileReader
	:members:

Functions
===================================

.. autoclass:: PySAM.WaveFileReader.WaveFileReader
	:members:

WeatherReader Group
======================================================

.. autoclass:: PySAM.WaveFileReader.WaveFileReader.WeatherReader
	:members:

Outputs Group
======================================================

.. autoclass:: PySAM.WaveFileReader.WaveFileReader.Outputs
	:members:

