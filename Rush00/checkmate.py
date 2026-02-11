def checkmate(board_string):
    
    board = [line.strip() for line in board_string.strip().split('\n') if line.strip()]
    
    if not board:
        return
    
    size = len(board)
    
    for r in board:
        if len(r) != size:
            return 

    if sum(row.count('K') for row in board) != 1:
        return
        
    king_count = sum(row.count('K') for row in board)
    if king_count != 1:
        return
    
    king_pos = None
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
            
    
    if not king_pos:
        return

    kr, kc = king_pos

    
    directions = {
        "straight": [(-1, 0), (1, 0), (0, -1), (0, 1)], # บน, ล่าง, ซ้าย, ขวา
        "diagonal": [(-1, -1), (-1, 1), (1, -1), (1, 1)] # ทะแยง 4 มุม
    }

    
    for dr, dc in directions["straight"]:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            if piece != '.': 
                break
            r += dr
            c += dc

    
    for dr, dc in directions["diagonal"]:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            if piece != '.':
                break
            r += dr
            c += dc

    
    pawn_checks = [(-1, -1), (-1, 1)]
    for dr, dc in pawn_checks:
        r, c = kr + dr, kc + dc
        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == 'P':
                print("Success")
                return

    
    print("Fail")