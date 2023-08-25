def main():
    workhours = int(input('Enter your work hours: '))
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78

   ##################################################
   # Code your program here
   ##################################################
    # overtime = workhours - reg_hours
    # overtime_wage = overtime * ov_rate
    # regular_wage = reg_hours * reg_rate
    # total_wage = regular_wage + overtime_wage

    if workhours > reg_hours:
        overtime_hours = workhours - reg_hours
        regular_wage = reg_hours * reg_rate
        overtime_wage = overtime_hours * ov_rate
    else:
        overtime_hours = 0
        regular_wage = workhours * reg_rate
        overtime_wage = 0


    total_wage = regular_wage + overtime_wage

    print(f"\nRegular hours: {reg_hours} Regular Charge: {regular_wage}")
    print(f"Overtime hours: {overtime_hours} Overtime Charge: {overtime_wage:.2f}\n")
    print(f"Total wage : {total_wage:.2f}")

   ##################################################
   # Do not delete the return statement
   ##################################################
    return regular_wage, overtime_wage, total_wage


if __name__ == '__main__':
    main()
