from ortools.algorithms.python import knapsack_solver
import time

class ClassicalKnapsackSolver:
    def __init__(self):
        # We use the branch and bound solver, which is exact and efficient for typical problems.
        self.solver = knapsack_solver.KnapsackSolver(
            knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
            'KnapsackExample'
        )

    def solve(self, values, weights, capacities):
        """
        Solves the knapsack problem and records execution time.
        """
        start_time = time.perf_counter()
        
        self.solver.init(values, weights, capacities)
        computed_value = self.solver.solve()
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        packed_items = []
        packed_weights = []
        total_weight = 0
        
        for i in range(len(values)):
            if self.solver.best_solution_contains(i):
                packed_items.append(i)
                packed_weights.append(weights[0][i])
                total_weight += weights[0][i]

        return {
            "total_value": computed_value,
            "total_weight": total_weight,
            "packed_items": packed_items,
            "execution_time_seconds": execution_time
        }