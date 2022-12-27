class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initalize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invaison in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        """Initalize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit