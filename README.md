Description for Timetable Generator Using Genetic Algorithm

Objective

The primary objective of this project is to automate timetable generation, reducing manual effort and 
scheduling time. The system aims to optimize timetables using Genetic Algorithms (GAs) to meet essential 
requirements, ensure constraint satisfaction, enhance scheduling efficiency, and provide a user-friendly 
interface. It is also designed to be scalable, handling various course sizes and complexities. 

Methodology 

The project employs a Genetic Algorithm for timetable generation. The process begins with initializing a 
population of potential solutions (chromosomes) based on input data like class schedules and room 
availability. The Evolution Loop iteratively improves these solutions through selection, crossover, and 
mutation phases, guided by a fitness function that evaluates how well each timetable meets scheduling 
constraints. The loop continues until a termination condition is met, such as reaching a maximum number of 
generations or achieving a satisfactory fitness level. The algorithm then outputs the best timetable as the 
optimal solution. 

Tools Used
  
--Python: Main programming language for developing the system. 

--PyYAML: Loads and parses input data from `raw_data.yml`. 

--Numpy: Handles numerical computations and array manipulations. 

--Pandas: Facilitates data manipulation and analysis. 

--Random: Introduces randomness in GA processes. 

--SciPy: Provides additional optimization algorithms and functionalities to enhance GA performance. 

Results 

Upon clicking the "Display best timetable" button, the system displays the timetable with the highest fitness 
score of 0.98. This indicates that the generated timetable optimally meets scheduling constraints, including 
minimizing class and room conflicts. The automated approach significantly reduces manual scheduling effort 
and time, producing efficient and practical schedules. 
