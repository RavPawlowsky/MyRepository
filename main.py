print("Welcome to Attachments Matrix for UK & GIB contracts!")

needed_dox = ""
UK_GIB = input("\nUK or GIB?\n").lower()
# tylko UK
if UK_GIB == "uk":
    bonuses = input(
        "\nPlease input all the bonuses separated by a coma. Type 'none' if there are no bonuses.\n").lower()
    platform = input("\nPlatform yes or no?\n").lower()
    if UK_GIB == "uk":
        contract_type = input("\nWhich contract type? Permanent of FTC?\n").lower()  # pytamy o contract type
        if contract_type != "ftc":  # jezeli kontrakt type jest inny, niz ftc - pytamy o grade (przy ftc nie ma takiej potrzeby)
            grade = input("\nWhich grade?\n").lower()
            needed_dox += f"\n- Contract template: Admin Team/Offer & Contract Management/Specialist Offer Pack/UK Group & Online Templates/Grade {grade.upper()} Contract"
            if grade == "4":
                needed_dox += "\n- My Rewards User Guide D"
            else:
                needed_dox += "\n- My Rewards User Guide E"

        else:  # co jesli ftc
            needed_dox += "- Admin Team/Offer & Contract Management/Specialist Offer Pack/UK Group & Online Templates/Fixed Term Contract"
            needed_dox += "\n- My Rewards User Guide E"

    # pierwszy plik kontraktowy dla UK Done

    # cover letter:
    if "on call" not in bonuses or platform == "yes":
        needed_dox += "\n- Admin Team/Offer & Contract Management/Specialist Offer Pack/UK Group & Online Templates/Cover Letter Templates"
    elif "on call" in bonuses and UK_GIB == "uk":
        needed_dox += "\n- Admin Team/Offer & Contract Management/Specialist Offer Pack/UK Group & Online Templates/Cover Letter Templates/COVER LETTER FOR ON CALL ALLOWANCE"
        # platform!

    if "on call" in bonuses and UK_GIB == "uk" and contract_type == "permanent" and grade != "6":
        if platform == "no":
            needed_dox += f"\n- Admin Team/Offer & Contract Management/Attachments UK & GIB/On Call Policy Grade {grade}"
    elif "on call" in bonuses and UK_GIB == "uk" and contract_type == "permanent" and grade == "6":
        if platform == "no":
            needed_dox += f"\n- Admin Team/Offer & Contract Management/Attachments UK & GIB/On Call Policy Grade 6"
    elif "on call" in bonuses and UK_GIB == "uk" and contract_type == "ftc":
        if platform == "no":
            needed_dox += f"\n- Admin Team/Offer & Contract Management/Attachments UK & GIB/On Call Policy Grade 6"
        else:
            needed_dox += "\n- DO NOT attach On Call Policy Attachment (no on call attachment for PLATFORM roles)"
    # if "on call" in bonuses and UK_GIB_GP == "uk" and platform == "no":
    #  needed_dox += "\n- Admin Team/Offer & Contract Management/Attachments UK & GIB/On Call Policy for relevant grade"
    # elif "on call" in bonuses and UK_GIB_GP == "uk" and platform == "yes":
    #  needed_dox += "\n- DO NOT attach On Call Policy Attachment (no on call attachment for PLATFORM roles)"
    # ale jesli platform to zwykly

    # if contract_type != "ftc" and grade == "4":
    #  needed_dox += "\n- My Rewards User Guide D"
    # elif contract_type == "ftc" or grade == "5" or grade == "6" or grade == "ptg":
    # needed_dox += "\n- My Rewards User Guide E"

    if contract_type == "ftc":
        print("\n- Confirm with REC which Bonus Scheme to attach, as the grade may differ for FTC.")
    elif contract_type == "permanent":
        needed_dox += f"\n- Bonus Scheme for {grade} grade"
    needed_dox += "\n- New Starter Checklist"
    print(needed_dox)

# teraz gib
if UK_GIB == "gib":
    bonuses = input(
        "\nPlease input all the bonuses separated by a coma. Type 'none' if there are no bonuses.\n").lower()
    if "on call" in bonuses:
        platform = input("\nPlatform yes or no?\n").lower()
    if UK_GIB == "gib":
        contract_type = input("\nWhich contract type? Permanent of FTC?\n").lower()  # pytamy o contract type
        if contract_type != "ftc":  # jezeli kontrakt type jest inny, niz ftc - pytamy o grade (przy ftc nie ma takiej potrzeby)
            grade = input("\nWhich grade?\n").lower()

if contract_type == "permanent" and grade != "6" and UK_GIB == "gib":
    print(
        "\n- Contract template: Admin Team/Offer & Contract Management/Specialist Offer Pack/Gibraltar Templates/GIB Contract & Cover Letter/.JC Reviewed - Template - 4,5,PTG - to use for contracts")
elif contract_type == "permanent" and grade == "6" and UK_GIB == "gib":
    print(
        "\n- Contract template: Admin Team/Offer & Contract Management/Specialist Offer Pack/Gibraltar Templates/GIB Contract & Cover Letter/AMS13 - GIB Contract for other grades")
elif contract_type == "ftc" and UK_GIB == "gib":
    print(
        "\n- Contract template: Admin Team/Offer & Contract Management/Specialist Offer Pack/Gibraltar Templates/GIB Fixed Term Contract & Cover Letter Templates/AMS15 - GIB FTC")

if contract_type == "permanent" and UK_GIB == "gib":
    print(
        "\n- Contract template: Admin Team/Offer & Contract Management/Specialist Offer Pack/Gibraltar Templates/GIB Contract & Cover Letter/.AMS 14 - GIB Cover Letter")
elif contract_type == "ftc" and UK_GIB == "gib":
    print(
        "\n- Contract template: Admin Team/Offer & Contract Management/Specialist Offer Pack/Gibraltar Templates/GIB Fixed Term Contract & Cover Letter Templates/AMS16 - GIB FTC external Cover Letter")

if "on call" in bonuses and UK_GIB == "gib":
    if platform == "no":
        needed_dox += f"\n- Admin Team/Offer & Contract Management/Attachments UK & GIB/On Call Policy Grade {grade}"
    else:
        needed_dox += "\n- DO NOT attach On Call Policy Attachment (no on call attachment for PLATFORM roles)"

if UK_GIB == "gib":
    print("\n- Admin Team/Offer & Contract Management/Attachments UK & GIB/Employee Privacy Notice")
