# Updated code
# Define the different pipeline stages

class FetchStage:
    def __init__(self):
        self.instruction = None

    def fetch(self, instruction):
        self.instruction = instruction
        print(f"Fetching instruction: {instruction}")
        return self.instruction

class DecodeStage:
    def __init__(self):
        self.decoded_instruction = None

    def decode(self, instruction):
        self.decoded_instruction = f"Decoded({instruction})"
        print(f"Decoding instruction: {instruction}")
        return self.decoded_instruction

class ExecuteStage:
    def __init__(self):
        self.result = None

    def execute(self, decoded_instruction):
        self.result = f"Executed({decoded_instruction})"
        print(f"Executing instruction: {decoded_instruction}")
        return self.result

class MemoryStage:
    def __init__(self):
        self.memory_access = None

    def access_memory(self, result):
        self.memory_access = f"Memory({result})"
        print(f"Memory access for: {result}")
        return self.memory_access

class WritebackStage:
    def __init__(self):
        self.writeback_result = None

    def writeback(self, memory_access):
        self.writeback_result = f"Writeback({memory_access})"
        print(f"Writing back result: {memory_access}")
        return self.writeback_result

# Define Branch Predictor
class BranchPredictor:
    def predict(self, instruction):
        if "BRANCH" in instruction:
            prediction = "Not Taken"
            print(f"Branch prediction for {instruction}: {prediction}")
            return prediction
        return None

# Defining the Basic Pipeline with Performance Metrics Collection
class BasicPipeline:
    def __init__(self):
        self.fetch_stage = FetchStage()
        self.decode_stage = DecodeStage()
        self.execute_stage = ExecuteStage()
        self.memory_stage = MemoryStage()
        self.writeback_stage = WritebackStage()
        self.instruction_count = 0
        self.total_cycles = 0
        self.latency_sum = 0

    def run_pipeline(self, instructions):
        for instruction in instructions:
            self.instruction_count += 1
            cycle_start = self.total_cycles

            fetched = self.fetch_stage.fetch(instruction)
            self.total_cycles += 1
            decoded = self.decode_stage.decode(fetched)
            self.total_cycles += 1
            executed = self.execute_stage.execute(decoded)
            self.total_cycles += 1
            memory_access = self.memory_stage.access_memory(executed)
            self.total_cycles += 1
            writeback = self.writeback_stage.writeback(memory_access)
            self.total_cycles += 1

            cycle_end = self.total_cycles
            latency = cycle_end - cycle_start
            self.latency_sum += latency
            print(f"Instruction {instruction} completed in {latency} cycles")

        throughput = self.instruction_count / self.total_cycles
        avg_latency = self.latency_sum / self.instruction_count
        print(f"Total Cycles: {self.total_cycles}")
        print(f"Throughput: {throughput} instructions per cycle")
        print(f"Average Latency: {avg_latency} cycles per instruction")

# Defining the Basic Pipeline with Branch Prediction
class BasicPipelineWithBranchPrediction(BasicPipeline):
    def __init__(self):
        super().__init__()
        self.branch_predictor = BranchPredictor()

    def run_pipeline(self, instructions):
        for instruction in instructions:
            if "BRANCH" in instruction:
                prediction = self.branch_predictor.predict(instruction)
            super().run_pipeline([instruction])

# Sample instructions (mix of regular and branch)
instructions = ["ADD r1, r2, r3", "SUB r4, r5, r6", "BRANCH target", "MUL r7, r8, r9", "BRANCH target"]

# Running the Basic Pipeline
print("\nRunning Basic Pipeline without Branch Prediction:")
pipeline = BasicPipeline()
pipeline.run_pipeline(instructions)

# Running the Pipeline with Branch Prediction
print("\nRunning Basic Pipeline with Branch Prediction:")
pipeline_with_bp = BasicPipelineWithBranchPrediction()
pipeline_with_bp.run_pipeline(instructions)
