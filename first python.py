
def calculate_split_balances(event: str, cost: float, service_charge_pct: int, group_size: int) -> dict:
    """
    Core computational engine for PayUp. 
    Processes transactional metrics and returns an aggregated calculation state.
    """
    total_service_charge = cost * (service_charge_pct / 100.0)
    grand_total = cost + total_service_charge
    total_per_person = grand_total / group_size if group_size > 0 else 0.0

  
    return {
        "event_name": event,
        "base_cost": cost,
        "service_charge_rate": service_charge_pct,
        "calculated_service_charge": total_service_charge,
        "group_count": group_size,
        "cumulative_total": grand_total,
        "per_capita_share": total_per_person
    }

def main() -> None:
    print("========================================")
    print("--- PayUp Financial Balancing Engine ---")
    print("========================================\n")

    try:
        event = input("Enter the transaction event name: ").strip()
        cost_input = input("Enter the base cost amount ($): ").strip()
        cost = float(cost_input)

        charge_input = input("Enter service charge rate percentage (e.g., 30 for 30%): ").strip().strip("%")
        service_charge = int(charge_input) if charge_input else 0

        size_input = input("Enter total number of participants: ").strip()
        group_size = int(size_input)

        if group_size <= 0:
            print("[System Error]: Participant count must be greater than zero.")
            return

    except ValueError:
        print("[System Error]: Invalid numeric matrix input. Computation aborted.")
        return

    # Execute computation engine
    transaction_state = calculate_split_balances(event, cost, service_charge, group_size)

    # Output Structured Financial Report
    print("\n" + "---" * 14)
    print(f"Financial Ledger for Event: {transaction_state['event_name']}")
    print("---" * 14)
    print(f"Base Cost:               ${transaction_state['base_cost']:.2f}")
    print(f"Service Charge Rate:     {transaction_state['service_charge_rate']}%")
    print(f"Total Service Surcharge: ${transaction_state['calculated_service_charge']:.2f}")
    print(f"Group Volume Count:      {transaction_state['group_count']}")
    print(f"Grand Total Bill:        ${transaction_state['cumulative_total']:.2f}")
    print("---" * 14)
    print(f"Per Capita Allocation:   ${transaction_state['per_capita_share']:.2f}")
    print("---" * 14 + "\n")

if __name__ == "__main__":
    main()





